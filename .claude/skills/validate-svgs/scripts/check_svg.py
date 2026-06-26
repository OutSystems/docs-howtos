#!/usr/bin/env python3
"""Check an SVG file against the OutSystems docs SVG visual spec.

Usage:
  python check_svg.py <path/to/file.svg>

Output: JSON with findings per category:
  {
    "attributes": {"verdict": "pass|fail", "issues": [...]},
    "colors":     {"verdict": "pass|fail", "issues": [...]},
    "naming":     {"verdict": "pass|fail", "type": "...", "issues": [...]},
    "dimensions": {"verdict": "pass|fail", "issues": [...]},
    "highlights": {"verdict": "pass|fail", "issues": [...]}
  }
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

# ---------------------------------------------------------------------------
# Approved color palette (lowercase 6-digit hex)
# ---------------------------------------------------------------------------
APPROVED_COLORS: frozenset[str] = frozenset({
    # Core
    "#f5f6fa", "#1783ef", "#686e76", "#0a141e", "#ffffff", "#f22800",
    # Extended
    "#66aaf7", "#dcecfd", "#e98223", "#14b775", "#d9d9d9", "#979ca2",
    "#00802d",
    # Hand cursor component
    "#0b0b18", "#f4f4f7",
    # ODC/Service Studio panel background
    "#f7f8fa",
    # Architecture diagram colors
    "#123661", "#157df3", "#add1fb", "#c6c9ce",
    # ODC logo colors (also approved directly)
    "#1f1f1f", "#ed1c24", "#eeeeee", "#ff8088",
    # ODC Portal UI dark background colors
    "#18191d", "#181a1f", "#2d2f36",
    # ODC Portal dark UI element
    "#24262b",
    # Cursor-black component
    "#43434e", "#b3b3b8", "#c8c9cd", "#d6d6d8", "#e1e1e3", "#e5e6e7",
    # TK Design system colors
    "#f85e40", "#f22800", "#db2400", "#fed06b", "#fdb515", "#d99b11",
    "#bb1f00", "#38bdff", "#0077b2", "#2dd267", "#00802d", "#ffffff",
    "#f5f6fa", "#c6c9ce", "#979ca2", "#686e76", "#0a141e", "#000000",
    "#0093d3", "#e18800", "#237131",
    # Service Studio platform icon colors
    "#0066db", "#006de9", "#025cc3", "#159570", "#18a0fb", "#3c92e8",
    "#41761a", "#428fdc", "#449604", "#47831a", "#626568", "#68d4f8",
    "#74e4a2", "#87898d", "#9475db", "#b5331e", "#beb0f4", "#cb371f",
    "#e53518", "#ec5941", "#ffc700",
    # Universal
    "#000000",
})

# Non-hex values that are always valid
ALWAYS_VALID_VALUES: frozenset[str] = frozenset({
    "none", "transparent", "inherit", "currentcolor",
})

# Common CSS named colors mapped to their hex equivalents for palette checking
NAMED_COLOR_MAP: dict[str, str] = {
    "black": "#000000",
    "white": "#ffffff",
    "red": "#ff0000",
    "green": "#008000",
    "blue": "#0000ff",
    "yellow": "#ffff00",
    "orange": "#ffa500",
    "purple": "#800080",
    "pink": "#ffc0cb",
    "gray": "#808080",
    "grey": "#808080",
    "silver": "#c0c0c0",
    "navy": "#000080",
    "teal": "#008080",
    "aqua": "#00ffff",
    "cyan": "#00ffff",
    "lime": "#00ff00",
    "maroon": "#800000",
    "olive": "#808000",
    "fuchsia": "#ff00ff",
    "magenta": "#ff00ff",
}

# ---------------------------------------------------------------------------
# Recognized suffixes
# ---------------------------------------------------------------------------
SCREENSHOT_SUFFIXES: frozenset[str] = frozenset({
    "ss", "odcs", "pl", "lt", "sc", "usr", "fg", "at", "ct", "af",
    "gc", "ams", "ib", "eb", "we", "wb", "az", "vs", "ok", "fc",
    "sa", "is", "ati", "uidp", "shc",
})
DIAGRAM_SUFFIX = "diag"

# ODC logo color fingerprint — these four colors appear together when an SVG
# contains the ODC logotype. When ≥ 2 of them are the only unapproved colors
# in a diagram, they come from the logo and are correct.
ODC_LOGO_COLORS: frozenset[str] = frozenset({
    "#1f1f1f", "#ed1c24", "#eeeeee", "#ff8088",
})

# ---------------------------------------------------------------------------
# PII patterns
# ---------------------------------------------------------------------------
_TEXT_CONTENT_TAGS: frozenset[str] = frozenset({
    "text", "tspan", "title", "desc",
    "flowRoot", "flowPara", "flowSpan",
})

_EMAIL_RE: re.Pattern = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
    re.IGNORECASE,
)

# Conservative phone pattern: requires a + prefix (international) or a
# parenthesised area code to avoid false positives on version numbers and IDs.
_PHONE_RE: re.Pattern = re.compile(
    r"(?<!\d)"
    r"(?:"
    r"\+\d{1,3}[\s\-]?\(?\d{1,4}\)?[\s\-]\d{3,5}[\s\-]\d{3,5}"
    r"|"
    r"\(\d{3}\)[\s\-]?\d{3}[\s\-\.]\d{4}"
    r")"
    r"(?!\d)"
)

# Internal OutSystems environment URLs, hostnames, and ticket IDs.
# *.outsystems.dev is always internal; only staging-style subdomains on
# outsystems.app are flagged (public training environments like
# training-prd.outsystems.app are not matched). eng-stage-* is flagged
# with or without a domain suffix. Private RFC-1918 IPs, localhost, and
# internal Jira ticket IDs (RDTKF-*, TK-*) are also caught.
_INTERNAL_URL_RE: re.Pattern = re.compile(
    r"(?:"
    r"[a-z0-9][a-z0-9\-]*\.outsystems\.dev"
    r"|(?:eng-stage|qa|staging|dev|internal)-[a-z0-9\-]*\.outsystems\.app"
    r"|eng-stage-[a-z0-9\-]+"
    r"|\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    r"|192\.168\.\d{1,3}\.\d{1,3}"
    r"|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b"
    r"|\blocalhost\b"
    r"|\b(?:RDTKF|TK)-\d+\b"
    r")",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Color-bearing XML attributes and CSS properties
# ---------------------------------------------------------------------------
COLOR_XML_ATTRS = (
    "fill", "stroke", "stop-color", "flood-color", "lighting-color", "color",
)
COLOR_CSS_PROPS = (
    "fill", "stroke", "stop-color", "flood-color", "lighting-color", "color",
    "background-color",
)
HEX_RE = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})(?=[^0-9a-fA-F]|$)")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize_hex(raw: str) -> str | None:
    """Return lowercase 6-digit hex, or None if not a valid hex color."""
    raw = raw.strip().lower()
    if not raw.startswith("#"):
        return None
    h = raw[1:]
    if len(h) == 3:
        h = h[0] * 2 + h[1] * 2 + h[2] * 2
    if len(h) == 6:
        return "#" + h
    return None


def closest_approved(color: str) -> str | None:
    """Return the approved color with the smallest Euclidean RGB distance."""
    norm = normalize_hex(color)
    if norm is None:
        return None
    try:
        r = int(norm[1:3], 16)
        g = int(norm[3:5], 16)
        b = int(norm[5:7], 16)
    except ValueError:
        return None

    best: str | None = None
    best_dist = float("inf")
    for approved in APPROVED_COLORS:
        try:
            ar, ag, ab = int(approved[1:3], 16), int(approved[3:5], 16), int(approved[5:7], 16)
        except (ValueError, IndexError):
            continue
        dist = ((r - ar) ** 2 + (g - ag) ** 2 + (b - ab) ** 2) ** 0.5
        if dist < best_dist:
            best_dist = dist
            best = approved
    return best


def parse_px(val: str | None) -> float | None:
    """Parse '1650', '1650px', '1650pt' etc. to a float."""
    if val is None:
        return None
    val = val.strip()
    for suffix in ("px", "pt", "em", "rem", "%"):
        if val.endswith(suffix):
            val = val[: -len(suffix)]
    try:
        return float(val)
    except ValueError:
        return None


def strip_ns(tag: str) -> str:
    """Remove XML namespace prefix: {http://...}rect -> rect."""
    return tag.split("}")[-1] if "}" in tag else tag


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_attributes(root: ET.Element, raw: str) -> list[str]:
    issues: list[str] = []

    # xmlns — ElementTree strips it; check raw text
    if 'xmlns=' not in raw and 'xmlns =' not in raw:
        issues.append('Missing `xmlns="http://www.w3.org/2000/svg"` on the root <svg> element.')

    # viewBox
    if root.get("viewBox") is None:
        issues.append("Missing `viewBox` attribute on the root <svg> element.")

    # width / height
    if root.get("width") is None:
        issues.append("Missing `width` attribute on the root <svg> element.")
    if root.get("height") is None:
        issues.append("Missing `height` attribute on the root <svg> element.")

    # xmlns:xlink required when xlink:href is used
    uses_xlink = "xlink:href" in raw or "xlink:" in raw
    has_xlink_ns = "xmlns:xlink" in raw
    if uses_xlink and not has_xlink_ns:
        issues.append(
            'Uses `xlink:href` but `xmlns:xlink="http://www.w3.org/1999/xlink"` '
            "is not declared on the root <svg> element."
        )

    return issues


def resolve_color_value(val: str) -> list[str]:
    """Return a list of hex color strings to check from a raw color value."""
    val_stripped = val.strip()
    val_lower = val_stripped.lower()

    if not val_stripped or val_lower in ALWAYS_VALID_VALUES or val_lower.startswith("url("):
        return []

    # Resolve named colors to hex for palette comparison
    if val_lower in NAMED_COLOR_MAP:
        return [NAMED_COLOR_MAP[val_lower]]

    # Extract hex values
    found = []
    for m in HEX_RE.finditer(val_stripped):
        found.append("#" + m.group(1))
    return found


def extract_colors(element: ET.Element) -> list[str]:
    """Collect all color values declared on a single element."""
    found: list[str] = []

    for attr in COLOR_XML_ATTRS:
        val = (element.get(attr) or "").strip()
        found.extend(resolve_color_value(val))

    style = (element.get("style") or "")
    for prop in COLOR_CSS_PROPS:
        m = re.search(rf"\b{re.escape(prop)}\s*:\s*([^;]+)", style, re.IGNORECASE)
        if m:
            found.extend(resolve_color_value(m.group(1)))

    return found


def check_colors(root: ET.Element) -> tuple[list[str], set[str]]:
    """Return (issues, unknown_hexes) — unknown_hexes is the set of unapproved colors found."""
    unknown: dict[str, dict] = {}

    for element in root.iter():
        for raw_color in extract_colors(element):
            norm = normalize_hex(raw_color)
            if norm is None:
                continue
            if norm in APPROVED_COLORS:
                continue
            if norm not in unknown:
                tag = strip_ns(element.tag)
                unknown[norm] = {
                    "tag": tag,
                    "closest": closest_approved(norm),
                    "count": 0,
                }
            unknown[norm]["count"] += 1

    issues: list[str] = []
    for color, info in sorted(unknown.items()):
        msg = f"Color `{color}` is not in the approved palette"
        if info["closest"]:
            msg += f" — closest approved color: `{info['closest']}`"
        if info["count"] > 1:
            msg += f" ({info['count']} occurrences)"
        msg += "."
        issues.append(msg)

    return issues, set(unknown.keys())


def check_naming(svg_path: str) -> dict:
    path = Path(svg_path)
    stem = path.stem
    parts = stem.split("-")
    suffix = parts[-1].lower() if parts else ""

    # Files NOT in an "images/" folder are shared assets (icons, logos,
    # illustrations). They don't follow the content-suffix convention.
    path_parts = path.parts
    if "images" not in path_parts:
        return {"verdict": "pass", "type": "icon_or_illustration", "issues": []}

    if suffix == DIAGRAM_SUFFIX:
        return {"verdict": "pass", "type": "diagram", "issues": []}
    if suffix in SCREENSHOT_SUFFIXES:
        return {"verdict": "pass", "type": "screenshot", "issues": []}
    if not suffix or stem == suffix:
        # Single-word name with no hyphen — icon/illustration
        return {"verdict": "pass", "type": "icon_or_illustration", "issues": []}

    # Unrecognized suffix on a content SVG
    return {
        "verdict": "fail",
        "type": "unknown",
        "issues": [
            f"Filename ends in `-{suffix}` which is not a recognized suffix. "
            f"Use a recognized screenshot suffix (e.g. `-ss`, `-odcs`, `-pl`) "
            f"or `-diag` for diagrams. "
            f"If this is an icon or illustration, remove the suffix entirely."
        ],
    }


def check_dimensions(root: ET.Element, svg_path: str) -> list[str]:
    stem = Path(svg_path).stem
    parts = stem.split("-")
    suffix = parts[-1].lower() if parts else ""

    if suffix != DIAGRAM_SUFFIX:
        return []

    width: float | None = parse_px(root.get("width"))

    if width is None:
        vb = (root.get("viewBox") or "").strip().split()
        if len(vb) == 4:
            width = parse_px(vb[2])

    if width is not None and width > 1650:
        return [
            f"Diagram width is {width:.0f}px — exceeds the 1650px maximum. "
            f"Resize to 1650px wide or narrower."
        ]
    return []


def check_highlights(root: ET.Element) -> list[str]:
    RED_NORM = "#f22800"
    issues: list[str] = []

    for element in root.iter():
        if strip_ns(element.tag) != "rect":
            continue

        fill_raw = (element.get("fill") or "none").strip()
        stroke_raw = (element.get("stroke") or "none").strip()

        fill_norm = normalize_hex(fill_raw) or fill_raw.lower()
        stroke_norm = normalize_hex(stroke_raw) or stroke_raw.lower()

        if fill_norm != RED_NORM and stroke_norm != RED_NORM:
            continue

        # ---- Validate stroke width when stroke is red ----
        if stroke_norm == RED_NORM:
            sw_raw = element.get("stroke-width", "1")
            try:
                sw = float(sw_raw)
            except (ValueError, TypeError):
                sw = 1.0
            if sw < 1 or sw > 6:
                issues.append(
                    f"Red highlight `stroke-width` is {sw} — "
                    f"expected 1–6px for a standard highlight rectangle."
                )

        # ---- Validate fill: solid red fill should be semi-transparent or elongated ----
        if fill_norm == RED_NORM:
            try:
                fill_opacity = float(element.get("fill-opacity") or element.get("opacity") or "1")
            except (ValueError, TypeError):
                fill_opacity = 1.0

            if fill_opacity >= 0.9:
                w = parse_px(element.get("width"))
                h = parse_px(element.get("height"))
                if w and h and w > 5 and h > 5:
                    ratio = max(w, h) / min(w, h) if min(w, h) > 0 else 99
                    if ratio < 2:
                        issues.append(
                            f"Red <rect> ({w:.0f}×{h:.0f}px) has a solid fill — "
                            f"highlights should use `stroke=\"#F22800\" fill=\"none\"` "
                            f"or a semi-transparent fill (`fill-opacity` < 0.9)."
                        )

    return issues


def check_connectors(root: ET.Element) -> list[str]:
    """Validate red <path>, <line>, <polyline>, <polygon> connectors/arrows."""
    RED_NORM = "#f22800"
    CONNECTOR_TAGS = {"path", "line", "polyline", "polygon"}
    issues: list[str] = []

    for element in root.iter():
        if strip_ns(element.tag) not in CONNECTOR_TAGS:
            continue

        fill_raw = (element.get("fill") or "none").strip()
        stroke_raw = (element.get("stroke") or "none").strip()

        fill_norm = normalize_hex(fill_raw) or fill_raw.lower()
        stroke_norm = normalize_hex(stroke_raw) or stroke_raw.lower()

        if fill_norm != RED_NORM and stroke_norm != RED_NORM:
            continue

        # Validate stroke-width when stroke is red
        if stroke_norm == RED_NORM:
            sw_raw = element.get("stroke-width", "1")
            try:
                sw = float(sw_raw)
            except (ValueError, TypeError):
                sw = 1.0
            if sw < 1 or sw > 6:
                tag = strip_ns(element.tag)
                issues.append(
                    f"Red connector <{tag}> `stroke-width` is {sw} — "
                    f"expected 1–6px for a standard connector."
                )

    return issues


def _collect_svg_text(root: ET.Element) -> str:
    """Collect all human-visible text from SVG text elements and aria-label attributes."""
    parts: list[str] = []
    for element in root.iter():
        tag = strip_ns(element.tag)
        if tag in _TEXT_CONTENT_TAGS:
            if element.text:
                parts.append(element.text)
            if element.tail:
                parts.append(element.tail)
        val = element.get("aria-label", "")
        if val:
            parts.append(val)
    return " ".join(parts)


def check_pii(root: ET.Element) -> tuple[list[str], str]:
    """Return (issues, verdict). Verdict is 'fail' for emails or internal URLs, 'warn' for phones only."""
    text = _collect_svg_text(root)
    email_issues: list[str] = []
    url_issues: list[str] = []
    phone_issues: list[str] = []
    seen: set[str] = set()

    for match in _EMAIL_RE.finditer(text):
        email = match.group(0)
        key = email.lower()
        if key not in seen:
            seen.add(key)
            email_issues.append(
                f"Email address `{email}` found in SVG text — replace with a "
                f"fictional or anonymized value before publishing."
            )

    for match in _INTERNAL_URL_RE.finditer(text):
        hit = match.group(0).strip()
        key = hit.lower()
        if key not in seen:
            seen.add(key)
            url_issues.append(
                f"Internal environment reference `{hit}` found in SVG text — "
                f"replace with a public demo URL or remove before publishing."
            )

    for match in _PHONE_RE.finditer(text):
        phone = match.group(0).strip()
        if phone not in seen:
            seen.add(phone)
            phone_issues.append(
                f"Possible phone number `{phone}` found in SVG text — verify "
                f"it is not real personal data before publishing."
            )

    issues = email_issues + url_issues + phone_issues
    if email_issues or url_issues:
        verdict = "fail"
    elif phone_issues:
        verdict = "warn"
    else:
        verdict = "pass"
    return issues, verdict


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def run(svg_path: str) -> dict:
    path = Path(svg_path)
    if not path.exists():
        return {"error": f"File not found: {svg_path}"}

    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"error": str(exc)}

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return {"error": f"Invalid SVG XML: {exc}"}

    attr_issues = check_attributes(root, raw)
    color_issues, unknown_hexes = check_colors(root)
    naming_result = check_naming(svg_path)
    dim_issues = check_dimensions(root, svg_path)
    highlight_issues = check_highlights(root)
    connector_issues = check_connectors(root)
    pii_issues, pii_verdict = check_pii(root)

    # The text-only PII scanner cannot read content inside embedded raster
    # images. When a raster is present and the scan found nothing, downgrade
    # the verdict so the skill always surfaces a warning and prompts a vision
    # check rather than silently passing the file.
    if 'xlink:href="data:image/' in raw or "xlink:href='data:image/" in raw:
        if pii_verdict == "pass":
            pii_verdict = "warn"
            pii_issues.append(
                "Contains an embedded raster image — the PII text scan is "
                "incomplete. Perform a vision check on the embedded image to "
                "verify no email addresses, phone numbers, or IP addresses are "
                "visible before publishing."
            )

    is_diagram = naming_result.get("type") == "diagram"

    # For diagrams: suppress violations that are exclusively ODC logo colors.
    # When ≥ 2 of the known ODC logo fingerprint colors appear together, they
    # come from an embedded ODC logotype and are correct by design.
    if is_diagram and color_issues:
        logo_hits = unknown_hexes & ODC_LOGO_COLORS
        if len(logo_hits) >= 2:
            color_issues = [
                issue for issue in color_issues
                if not any(f"`{c}`" in issue for c in logo_hits)
            ]
            unknown_hexes = unknown_hexes - logo_hits

    colors_verdict = "fail" if color_issues else "pass"
    # Diagrams (-diag) may depict product UI in vector form using product brand
    # colors. Downgrade remaining violations to warnings so they are surfaced
    # but don't block review.
    if is_diagram and color_issues:
        colors_verdict = "warn"

    return {
        "attributes": {
            "verdict": "fail" if attr_issues else "pass",
            "issues": attr_issues,
        },
        "colors": {
            "verdict": colors_verdict,
            "issues": color_issues,
        },
        "naming": naming_result,
        "dimensions": {
            "verdict": "fail" if dim_issues else "pass",
            "issues": dim_issues,
        },
        "highlights": {
            "verdict": "fail" if highlight_issues else "pass",
            "issues": highlight_issues,
        },
        "connectors": {
            "verdict": "fail" if connector_issues else "pass",
            "issues": connector_issues,
        },
        "pii": {
            "verdict": pii_verdict,
            "issues": pii_issues,
        },
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: check_svg.py <path/to/file.svg>"}))
        sys.exit(1)
    print(json.dumps(run(sys.argv[1]), indent=2))
