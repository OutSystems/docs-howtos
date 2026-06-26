# SVG validation rubric

**Calibrated:** 2026-06-15 by Bernardo (deep exploration of training-internal
SVG corpus — diagrams, composite diagrams, screenshots, icons, illustrations).
Applicable across OutSystems docs repositories.

The skill uses this file as a checklist. Each rule has:

* **Severity** — `❌` means fail; `⚠️` means warn.
* **Check** — what the skill verifies on each SVG.

---

## 1. Required SVG attributes

* **Severity:** ❌
* **Check (scripted):** the root `<svg>` element must declare:
    * `xmlns="http://www.w3.org/2000/svg"` — standard SVG namespace
    * `viewBox` — enables proper scaling; all exported SVGs must include it
    * `width` and `height` — explicit pixel dimensions required
    * `xmlns:xlink="http://www.w3.org/1999/xlink"` — required when the file
      uses `xlink:href` for embedded raster images; omitting it breaks
      rendering in some environments
* **Verdict comes from `scripts/check_svg.py` (`attributes`).**

---

## 2. Naming — lowercase, hyphens, recognized suffix

* **Severity:** ❌
* **Check (scripted):** apply the following suffix logic to the filename stem
  (everything before `.svg`):
    * File is NOT inside an `images/` folder (for example, paths like
      `shared/outsystems/icons/`) → valid icon or illustration; skip all
      suffix checks for this file
    * Ends with a recognized screenshot suffix → valid screenshot
    * Ends with `-diag` → valid diagram
    * Has no suffix (e.g. `database.svg`, `done.svg`) → valid icon or
      illustration; no warning
    * Has an unrecognized suffix → flag as ❌ and suggest the correct suffix

  Recognized screenshot suffixes:
  `-ss` (Service Studio), `-odcs` (ODC Studio), `-pl` (ODC Portal),
  `-lt` (LifeTime), `-sc` (Service Center), `-usr` (Users), `-fg` (Forge),
  `-at`, `-ct`, `-af`, `-gc`, `-ams`, `-ib`, `-eb`, `-we`, `-wb`, `-az`,
  `-vs`, `-ok`, `-fc`, `-sa`, `-is`, `-ati`, `-uidp`, `-shc`

* **Check (vision, diagrams only):** for `-diag` files, vision verifies the
  content is consistent with a diagram or annotated composite rather than a
  plain bare product screenshot. If it looks like a plain screenshot with no
  diagram framing, flag ⚠️ and suggest a surface suffix.

* **Verdict comes from `scripts/check_svg.py` (`naming`).**

---

## 3. Approved color palette

* **Severity:** ❌
* **Check (scripted):** all `fill`, `stroke`, `stop-color`, `flood-color`,
  and inline `style` color declarations must use values from the approved
  extended palette below. Case-insensitive comparison.

  **Core palette:**

  | Color | Hex | Use |
  | --- | --- | --- |
  | Brand white | `#F5F6FA` | Light backgrounds |
  | Decision blue | `#1783EF` | Highlights, decisions |
  | Space-grey | `#686E76` | Containers, secondary text |
  | Dark text | `#0A141E` | Primary text, strokes |
  | Canvas | `#FFFFFF` | Canvas, white fills |
  | Red | `#F22800` | Highlights, accents |

  **Extended palette (also approved):**

  | Color | Hex | Use |
  | --- | --- | --- |
  | Light blue | `#66AAF7` | Diagram fills, backgrounds |
  | Pale blue | `#DCECFD` | Diagram backgrounds |
  | Orange | `#E98223` | Accent |
  | Green | `#14B775` | Success, positive state |
  | Light grey | `#D9D9D9` | Borders, secondary elements |
  | Medium grey | `#979CA2` | Secondary text, icons |
  | Dark green | `#00802D` | Success variant |
  | Icon grey | `#87898D` | Platform icon fills |
  | Deep navy | `#123661` | Architecture diagram shapes, arrows |
  | Sky blue | `#157df3` | Architecture diagram fills |
  | Pale blue tint | `#ADD1FB` | Architecture diagram backgrounds |
  | Soft grey | `#C6C9CE` | Architecture diagram borders |
  | ODC logo near-black | `#1F1F1F` | ODC logotype |
  | ODC logo red | `#ED1C24` | ODC logotype |
  | ODC logo off-white | `#EEEEEE` | ODC logotype |
  | ODC logo coral | `#FF8088` | ODC logotype |
  | ODC Portal dark bg | `#18191D` | ODC Portal dark UI background |
  | ODC Portal dark bg alt | `#181A1F` | ODC Portal dark UI background variant |
  | ODC Portal panel bg | `#2D2F36` | ODC Portal dark panel/sidebar background |
  | Studio panel bg | `#F7F8FA` | ODC Studio / Service Studio panel background |
  | ODC Portal dark element | `#24262b` | ODC Portal dark UI element (e.g. sidebar row hover) |
  | Cursor-black base | `#43434e` | Cursor-black component |
  | Cursor-black light-1 | `#b3b3b8` | Cursor-black component |
  | Cursor-black light-2 | `#c8c9cd` | Cursor-black component |
  | Cursor-black light-3 | `#d6d6d8` | Cursor-black component |
  | Cursor-black light-4 | `#e1e1e3` | Cursor-black component |
  | Cursor-black light-5 | `#e5e6e7` | Cursor-black component |

  **TK design system colors (also approved):**

  | Color | Hex | Use |
  | --- | --- | --- |
  | TK orange-red | `#F85E40` | Accent, highlights |
  | TK dark red | `#BB1F00` | Accent, error state |
  | TK yellow light | `#FED06B` | Warning, accent |
  | TK yellow | `#FDB515` | Warning, accent |
  | TK amber | `#D99B11` | Warning variant |
  | TK bright blue | `#38BDFF` | Accent, highlights |
  | TK dark blue | `#0077B2` | Links, actions |
  | TK blue | `#0093D3` | Accent, informational |
  | TK green | `#2DD267` | Success, positive state |
  | TK dark green | `#237131` | Success variant |
  | TK orange | `#E18800` | Accent, warning |

  **Service Studio platform icon colors (also approved):**

  | Color | Hex | Use |
  | --- | --- | --- |
  | SS blue | `#0066DB` | Service Studio icon fill |
  | SS blue variant | `#006DE9` | Service Studio icon fill |
  | SS blue dark | `#025CC3` | Service Studio icon fill |
  | SS teal green | `#159570` | Service Studio icon fill |
  | SS light blue | `#18A0FB` | Service Studio icon fill |
  | SS blue mid | `#3C92E8` | Service Studio icon fill |
  | SS dark green | `#41761A` | Service Studio icon fill |
  | SS blue soft | `#428FDC` | Service Studio icon fill |
  | SS green | `#449604` | Service Studio icon fill |
  | SS dark green alt | `#47831A` | Service Studio icon fill |
  | SS grey | `#626568` | Service Studio icon fill |
  | SS cyan | `#68D4F8` | Service Studio icon fill |
  | SS light green | `#74E4A2` | Service Studio icon fill |
  | SS icon grey | `#87898D` | Service Studio icon fill |
  | SS purple | `#9475DB` | Service Studio icon fill |
  | SS dark red | `#B5331E` | Service Studio icon fill |
  | SS light purple | `#BEB0F4` | Service Studio icon fill |
  | SS red | `#CB371F` | Service Studio icon fill |
  | SS red variant | `#E53518` | Service Studio icon fill |
  | SS orange-red | `#EC5941` | Service Studio icon fill |
  | SS yellow | `#FFC700` | Service Studio icon fill |

  **Always allowed:** `#000000`, `none`, `transparent`, `inherit`,
  `currentColor`.

* **ODC logo fingerprint — silently accepted:** the ODC logotype uses a
  specific set of four colors (`#1f1f1f`, `#ed1c24`, `#eeeeee`, `#ff8088`).
  These colors are also in the approved palette directly, so they pass
  unconditionally. The fingerprint suppression logic in `check_svg.py` is
  retained for backward compatibility but is now a no-op for these colors.

* **Diagram color violations are warnings, not errors:** files with the
  `-diag` suffix may depict product UI in vector form using product brand
  colors. After removing any ODC logo hits, remaining unapproved colors
  are downgraded to `⚠️` warnings rather than `❌` errors. Surface them
  with a note that they may be intentional product UI colors.

  Script reports each unknown color with its actual hex value and the closest
  approved alternative. **Verdict comes from `scripts/check_svg.py`
  (`colors`).**

* **Note:** `<filter>`, `<linearGradient>`, and `<radialGradient>` are
  explicitly **allowed** — they are widely used in the repo for drop shadows
  and architecture diagram fills. Check their color values, not their presence.

---

## 4. Diagram width — max 1650 px

* **Severity:** ❌
* **Check (scripted):** for files with the `-diag` suffix, the diagram width
  (from the `width` attribute, or from the third value of `viewBox`) must be
  ≤ 1650 px. Height is not constrained.
* **Note:** icons and illustrations have no size constraint.
* **Verdict comes from `scripts/check_svg.py` (`dimensions`).**

---

## 5. Red highlight structure (when present)

* **Severity:** ❌
* **Check (scripted, optional):** this rule only fires when `#F22800` is
  present in `<rect>` elements. It does not require highlights to exist.

  Valid highlight patterns:
    * `stroke="#F22800"` with `stroke-width` between 1 and 6 px and
    `fill="none"` — standard rectangle outline highlight
    * `fill="#F22800"` with `fill-opacity` < 0.9 — semi-transparent overlay

  What the script flags:
    * A `<rect>` with solid `fill="#F22800"` (opacity ≥ 0.9) that is not very
    elongated (width/height ratio < 2:1) — likely a solid block rather than a
    highlight stripe
    * `stroke-width` outside the 1–6 px range — too thin to be visible or too
    thick to look like a standard highlight

  **Verdict comes from `scripts/check_svg.py` (`highlights`).**

* **Note:** shadow, cursor/pointer, and numbered callouts are **not** required
  or checked in this repo. These differ from the `validate-screenshots` skill
  which applies to PNG docs screenshots.

---

## 6. PII — emails, phone numbers, IP addresses

* **Severity:** ❌ for email addresses; ⚠️ for phone numbers and IP addresses.
* **Check (scripted):** the script extracts all visible text from SVG `<text>`,
  `<tspan>`, `<title>`, `<desc>`, `flowRoot`/`flowPara`/`flowSpan` elements,
  and `aria-label` attributes, then searches for:
    * Email addresses (regex match on `user@domain.tld`) → `"fail"` verdict.
    * Phone numbers (international `+NNN…` or US `(NNN) NNN-NNNN` format) →
      `"warn"` verdict.
    * IPv4 addresses (four dot-separated octets, e.g. `192.168.1.1`) → `"warn"`
      verdict. The pattern excludes version strings and plain decimals.
* **Check (vision, embedded rasters):** SVGs that embed a PNG screenshot cannot
  have their raster text read by the script. The skill extracts the PNG and
  runs a vision scan for visible emails (❌), phone numbers (⚠️), and IP
  addresses (⚠️).
* **Verdict comes from `scripts/check_svg.py` (`pii`).**

---

## Rules the skill does not check

* **Drop shadow / outer frame:** not required for SVGs in training-internal.
* **Cursor / pointer:** not required.
* **Numbered callouts:** not used in this repo — no validation needed.
* **Theme (light vs dark):** not enforced for SVGs.
* **Internal URLs / hostnames:** checked by the `pii` script category (❌).
  Flags `eng-stage-*`, `qa-*`, `staging-*`, `internal-*` subdomains, and
  internal Jira ticket IDs (`RDTKF-*`, `TK-*`) in SVG text elements. Generic
  synthetic tenant names (e.g. `neo-apps.outsystems.dev`) and public demo URLs
  (e.g. `training-prd.outsystems.app`) are not flagged.
