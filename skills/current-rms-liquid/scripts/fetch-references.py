#!/usr/bin/env python3
"""Fetch and clean the official Current-RMS Liquid docs into references/.

The reference material is (c) Current RMS, so this public repo doesn't
redistribute it. Instead, this script downloads the docs from the official
GitBook site at install time (and can be re-run any time to pick up doc
updates). Requires Python 3 and an internet connection; no dependencies.

Usage:  python3 scripts/fetch-references.py
"""
import os
import re
import sys
import urllib.request

BASE = "https://current-rms.gitbook.io/liquid-syntax"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "references")
OBJ = os.path.join(REF, "objects")

# Topic pages that live at references/ top level under friendlier names.
TOPIC_NAMES = {
    "introduction/liquid-filters.md": "filters.md",
    "introduction/liquid-tags.md": "tags.md",
    "introduction/operators.md": "operators.md",
    "introduction/liquid-objects.md": "objects-basics.md",
    "introduction/best-practices.md": "best-practices.md",
    "information/attributes.md": "attributes-front-matter.md",
    "information/consolidation.md": "consolidation.md",
    "information/custom-fields.md": "custom-fields.md",
    "information/date-filter.md": "date-formats.md",
    "information/deal-pricing.md": "deal-pricing.md",
    "information/special-objects.md": "special-items.md",
    "pdf-renderer/pdf-generator.md": "pdf-limitations.md",
}
SKIP = {"master.md", "introduction/what-is-liquid-syntax.md"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "current-rms-liquid-skill"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def clean(text):
    lines = text.split("\n")
    while lines and (lines[0].startswith("> For the complete documentation index") or not lines[0].strip()):
        lines.pop(0)
    text = "\n".join(lines).replace("&#x20;", " ")

    def hint(m):
        label = {"warning": "Warning", "info": "Note", "danger": "Important",
                 "success": "Tip"}.get(m.group(1), "Note")
        quoted = "\n".join("> " + l for l in m.group(2).strip().split("\n"))
        return f"> **{label}:**\n{quoted}"

    text = re.sub(r'\{%\s*hint style="(\w+)"\s*%\}(.*?)\{%\s*endhint\s*%\}', hint, text, flags=re.S)
    text = re.sub(r'\{%\s*content-ref url="[^"]*"\s*%\}\s*(.*?)\s*\{%\s*endcontent-ref\s*%\}', r'See: \1', text, flags=re.S)
    text = re.sub(r'^!\[[^\]]*\]\(/files/[^)]*\)\s*$', '', text, flags=re.M)
    text = text.replace("](/liquid-syntax/", "](" + BASE + "/")
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + "\n"


def main():
    os.makedirs(OBJ, exist_ok=True)
    print("Fetching documentation index ...")
    llms = fetch(BASE + "/llms.txt")
    pages = re.findall(r'https://current-rms\.gitbook\.io/liquid-syntax/(\S+\.md)', llms)
    pages = [p for p in dict.fromkeys(pages) if p not in SKIP]
    print(f"Found {len(pages)} pages.")

    index = []
    for page in pages:
        try:
            out = clean(fetch(f"{BASE}/{page}"))
        except Exception as e:
            print(f"  FAILED {page}: {e}", file=sys.stderr)
            continue
        m = re.search(r'^# (.+)$', out, flags=re.M)
        title = m.group(1).strip() if m else page
        out += f"\n---\n*Source: [{title} — Current RMS Liquid docs]({BASE}/{page})*\n"
        if page in TOPIC_NAMES:
            dest = os.path.join(REF, TOPIC_NAMES[page])
        else:
            fn = page.replace("/", "__")
            dest = os.path.join(OBJ, fn)
            attrs = re.findall(r'^## [`*]*([^`*\n]+)[`*]*$', out, flags=re.M)
            index.append((fn, title, attrs))
        with open(dest, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"  ok  {page}")

    with open(os.path.join(REF, "object-index.md"), "w", encoding="utf-8") as f:
        f.write("# Current-RMS Liquid — object & attribute index\n\n")
        f.write("Every documented object and its attributes. If an attribute is not "
                "listed here or in the object's reference file, DO NOT use it.\n"
                "Full details per object: `references/objects/<file>`.\n\n")
        for fn, title, attrs in sorted(index, key=lambda x: x[0]):
            f.write(f"## {title}  (`objects/{fn}`)\n\n")
            f.write((", ".join(f"`{a.strip()}`" for a in attrs) or "(see file)") + "\n\n")

    print(f"\nDone. References written to {REF}")


if __name__ == "__main__":
    main()
