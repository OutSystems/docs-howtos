---
name: validate-svgs
description: >-
  Validates SVG visual assets in OutSystems docs repositories against the
  team's visual spec. Checks required SVG attributes, approved color palette,
  filename suffix conventions, diagram width limits, and red highlight
  structure. Returns an issues-only summary so the content developer knows
  whether the images are ready for review.

  Use whenever a content developer wants to check SVG files before merging,
  or asks to "validate SVGs", "review SVGs", "check my images", "validate
  visual assets", "check SVGs", "are these SVGs OK".

  Trigger phrases: "validate SVGs", "review SVGs", "check my SVGs", "check
  images", "validate visual assets", "are these SVGs OK", "review visual
  assets".
allowed-tools: Read,Bash,AskUserQuestion
metadata:
  exclude-repos:
    - OutSystems/docs-eap
    - OutSystems/docs-next
    - OutSystems/docs-product-internal
    - OutSystems/docs-support-internal
    - OutSystems/docs-validation
---

# Validate SVG files

Runs a visual-spec review on SVG files a content developer added or modified
in the training-internal repository, so they can self-check before asking for
manual design review.

The rubric lives in `visual-rules-svgs.md` next to this file. If it contains
the placeholder marker (`<!-- NOT CALIBRATED -->`), stop and tell the user the
rubric has not been set up yet.

## Setup

Read `visual-rules-svgs.md` from the same directory as this SKILL.md.

## Step 1: Resolve targets

Call the target collector with whatever the user passed (default to empty):

```
python3 -B <skill-dir>/scripts/collect_targets.py "$ARGUMENTS"
```

It prints a JSON array to stdout. Each entry has:

* `image_path` — absolute path to the SVG
* `article_path` — the markdown that references it, or `null`
* `sha256` — file hash for duplicate detection

If the array is empty, stop with:

> "No SVGs to validate. Pass a markdown file, an SVG path, or a folder — or
> run without arguments on a branch that has SVG changes vs. master."

### Duplicate detection

After collecting targets, group entries by their `sha256` field. If two or
more entries share a hash, the files are byte-for-byte identical and only
one copy should exist. Mark every duplicate with a ❌ finding:

> "Byte-identical duplicate of `<other filename>`. Keep one and delete the
> rest."

## Step 2: Validate each target

For each entry, run the script checker:

```
python3 -B <skill-dir>/scripts/check_svg.py "<image_path>"
```

The script outputs JSON with the following top-level keys, each containing
a `verdict` and an `issues` array of strings:

* `attributes` — required SVG declarations (xmlns, viewBox, width, height,
  xmlns:xlink when xlink:href is used); verdict `"pass"` or `"fail"`
* `colors` — all fill/stroke/stop-color values checked against the approved
  palette; each issue names the offending color and the closest approved
  alternative; verdict is `"pass"`, `"fail"`, or **`"warn"`**
* `naming` — filename suffix check; also includes a `type` field
  (`"screenshot"`, `"diagram"`, `"icon_or_illustration"`, or `"unknown"`)
* `dimensions` — width limit for `-diag` files (max 1650 px); verdict
  `"pass"` or `"fail"`
* `highlights` — red highlight rectangle structure when `#F22800` is present;
  verdict `"pass"` or `"fail"`
* `pii` — personal information in visible SVG text (email addresses, internal
  environment URLs/hostnames, phone numbers, IP addresses); verdict `"pass"`,
  `"fail"` (emails or internal URLs found), or `"warn"` (phone numbers or IP
  addresses found, no emails or internal URLs)

**Interpreting results:**

* Every non-empty `issues` string in `attributes`, `dimensions`, and
  `highlights` is a ❌ finding.
* A naming `"fail"` verdict is a ❌ finding.
* `colors.verdict == "fail"` → each color issue is a ❌ finding.
* `colors.verdict == "warn"` → each color issue is a ⚠️ warning. This
  happens for `-diag` files, which often depict product UI in vector form
  and intentionally use product brand colors. Mention this context in the
  summary note.
* `pii.verdict == "fail"` → each issue is a ❌ finding (email address or internal environment URL found).
* `pii.verdict == "warn"` → each issue is a ⚠️ warning (possible phone number
  or IP address; may be example data, but needs human review).
* **PII scan limitation:** the script can only read text declared as SVG `<text>`
  or `<tspan>` elements. For files that embed a rasterized PNG, run the vision
  check below instead of relying on the script verdict.
* Collect only failures/warnings — passing rules are not reported.
* Do not second-guess the script's color or dimension verdicts; it reads the
  raw XML values.

**Suffix-vs-content check (vision, diagram files only):**

For files where `naming.type == "diagram"` (suffix is `-diag`), read the file
with the Read tool so it goes into vision when possible. Use vision to verify
the content is consistent with a diagram (architecture, flow, annotation
composite) rather than a bare UI screenshot with no diagram framing. If the
content looks like a plain product screenshot with no compositional framing or
diagram elements, emit ⚠️:

> "File uses `-diag` suffix but looks like a plain product screenshot — rename
> with the correct surface suffix (e.g. `-ss`, `-odcs`)."

Skip this vision check if the Read tool cannot render the SVG.

**Vision PII check for embedded-raster files:**

After running the script for each file, check whether the SVG embeds a
rasterized image:

```
grep -c 'xlink:href="data:image/' "<image_path>"
```

If the count is 1 or more, the PII script cannot read text inside the embedded
image. Extract the PNG to a temp file and check it visually:

```
python3 -B -c "
import re, base64, sys
data = open(sys.argv[1]).read()
m = re.search(r'xlink:href=\"data:image/png;base64,([^\"]+)\"', data)
if m:
    open('/tmp/_pii_check.png', 'wb').write(base64.b64decode(m.group(1).replace(' ','').replace('\n','')))
    print('extracted')
else:
    print('none')
" "<image_path>"
```

* If the script prints `extracted`: Read `/tmp/_pii_check.png` with the Read
  tool so it goes into vision. Scan the rendered image for visible email
  addresses (e.g. `user@example.com`), phone numbers, or IP addresses
  (e.g. `192.168.1.1`). Report findings:
    * Email address visible → ⚠️ "Visible email address in embedded raster —
    review whether it is real data; remove or obscure before shipping."
    * Phone number visible → ⚠️ "Possible phone number in embedded raster —
    review whether it is real data."
    * IP address visible → ⚠️ "Possible IP address in embedded raster —
    review whether it is an internal address."
    * Nothing found → no finding needed.
* If the script prints `none`: no embedded PNG; skip this check.

After the vision check, delete the temp file:

```
rm -f /tmp/_pii_check.png
```

Skip this entire check when `grep` returns 0.

**Red highlight rules:** the script only flags issues when `#F22800` is
actually present in the file. It does **not** require highlights to be
present — skip this category entirely when `highlights.verdict == "pass"` and
`highlights.issues` is empty.

Keep per-file notes internal until every file is processed. Do not stream
partial reports.

### Extract the Figma link (once per article)

If any entry has a non-null `article_path`, open that markdown file once and
grep its YAML frontmatter for a `figma:` key (the value is a `figma.com` URL).
Remember the value — the report header will surface it so the content
developer can jump straight to Figma to fix things. If the frontmatter has no
`figma:` field, or the value is empty, skip the link entirely (don't print an
empty `Figma:` line).

When multiple articles reference different SVGs (branch-diff mode), collect the
unique Figma URLs per article and emit them grouped under each article in the
header. In the common single-article case, one line is enough.

## Step 3: Emit the summary

Follow this exact format:

```
## SVG review: <article filename or "branch changes">

Figma: <url from frontmatter — omit this line entirely when no figma key>

Checked N SVGs. M need changes.

### <image relative path>
- ❌ <short description of the failure — reference the rule>
- ⚠️ <short description of a warning>

### <next image path>
- ❌ <...>
```

Rules:

* If N > 0 and M == 0: replace the body with `All N SVGs pass.` and skip the
  per-file sections. Keep the `Figma:` line in the header if it was extracted.
* Severity: `❌` means "must fix before the article ships"; `⚠️` means "a
  designer should eyeball this, but it might be acceptable".
* Never list a rule that passed.
* Don't repeat the rubric text. Quote the rule name only if needed for
  clarity.
