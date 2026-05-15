"""
compile_wiki.py — Step 2 of the knowledge base workflow.

Reads all raw source files from raw/ and uses Claude to compile them
into a structured, linked markdown wiki in wiki/.
"""

import anthropic
import re
import sys
from pathlib import Path

RAW_DIR = Path("raw")
WIKI_DIR = Path("wiki")

WIKI_PLAN = """
- wiki/index.md                          (hub: overview + links to all articles)
- wiki/concepts/lease-terms.md           (lease types, key clauses, what to watch for)
- wiki/concepts/security-deposit.md      (rules, deductions, how to protect it)
- wiki/concepts/renters-insurance.md     (coverage, cost, how to get it)
- wiki/guides/move-in.md                 (inspection process, room-by-room checklist)
- wiki/guides/move-out.md                (timeline, cleaning checklist, written notice)
- wiki/guides/utilities-setup.md         (types of utilities, setup steps, cost estimates)
- wiki/guides/maintenance-requests.md    (categories of urgency, how to submit, follow-up)
- wiki/guides/landlord-communication.md  (written record tips, tone, follow-up)
- wiki/guides/parking-rules.md           (permit types, towing, what to ask before signing)
- wiki/templates/maintenance-email.md    (copy-paste email template for repairs)
- wiki/templates/move-out-notice.md      (copy-paste move-out notice template)
"""

SYSTEM_PROMPT = """You are building a structured markdown knowledge base for international students
navigating U.S. apartment rentals. Your output will be saved as individual .md files.

Rules for the wiki:
- Each article should have a clear title (# heading), helpful subheadings, and practical content.
- Cross-link related articles using [[article-name]] syntax (use the filename without extension).
- Include a "Related" section at the bottom of each article with 2–4 cross-links.
- Write in plain, friendly English appropriate for non-native speakers.
- Include warnings (⚠️), tips (💡), and key terms in **bold** where helpful.
- The index.md should be a navigation hub with a short description of each article.

Output format — wrap each file exactly like this, with no extra text between files:
<file name="wiki/index.md">
[content]
</file>
<file name="wiki/concepts/lease-terms.md">
[content]
</file>
... and so on for all 12 files."""


def read_raw_files() -> dict[str, str]:
    files = {}
    for f in sorted(RAW_DIR.glob("*.md")):
        files[f.name] = f.read_text(encoding="utf-8")
    return files


def build_raw_context(files: dict[str, str]) -> str:
    sections = []
    for name, content in files.items():
        sections.append(f"=== SOURCE FILE: {name} ===\n{content}")
    return "\n\n".join(sections)


def compile_wiki(raw_files: dict[str, str]) -> str:
    client = anthropic.Anthropic()

    raw_context = build_raw_context(raw_files)

    print("  Calling Claude API (this may take 30–60 seconds)...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": raw_context,
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "type": "text",
                        "text": (
                            f"Please compile the raw sources above into the following wiki files:\n{WIKI_PLAN}\n\n"
                            "Generate all 12 files now. Use [[filename]] cross-links generously."
                        ),
                    },
                ],
            }
        ],
    )

    usage = response.usage
    print(
        f"  Tokens — input: {usage.input_tokens}, output: {usage.output_tokens}"
        + (f", cache_read: {usage.cache_read_input_tokens}" if hasattr(usage, 'cache_read_input_tokens') else "")
    )
    return response.content[0].text


def save_wiki_files(compiled_text: str) -> int:
    pattern = r'<file name="([^"]+)">(.*?)</file>'
    matches = re.findall(pattern, compiled_text, re.DOTALL)

    if not matches:
        print("ERROR: Could not parse any <file> blocks from Claude's response.")
        print("Raw response saved to outputs/compile_debug.txt")
        Path("outputs").mkdir(exist_ok=True)
        Path("outputs/compile_debug.txt").write_text(compiled_text)
        return 0

    for filepath, content in matches:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"  Saved: {filepath}")

    return len(matches)


def main():
    print("=== compile_wiki.py: Building Knowledge Base ===\n")

    print(f"Step 1: Reading raw source files from {RAW_DIR}/")
    raw_files = read_raw_files()
    if not raw_files:
        print(f"ERROR: No .md files found in {RAW_DIR}/. Exiting.")
        sys.exit(1)
    for name in raw_files:
        print(f"  - {name}")
    print()

    print("Step 2: Compiling wiki with Claude...")
    compiled_text = compile_wiki(raw_files)
    print()

    print(f"Step 3: Saving wiki files to {WIKI_DIR}/")
    count = save_wiki_files(compiled_text)
    print()

    if count > 0:
        print(f"Done! {count} wiki files created in wiki/")
        print("Next steps:")
        print("  python ask.py \"What should I do before signing a lease?\"")
        print("  python lint.py")
    else:
        print("Compilation failed. Check outputs/compile_debug.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
