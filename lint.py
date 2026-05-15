"""
lint.py — Step 4: Knowledge base health check.

Analyzes the compiled wiki for quality issues, missing links,
inconsistencies, and improvement opportunities.

Usage:
    python lint.py
"""

import anthropic
import sys
from pathlib import Path

WIKI_DIR = Path("wiki")
OUTPUTS_DIR = Path("outputs")

LINT_PROMPT = """You are reviewing a markdown knowledge base about U.S. apartment rentals
for international students. Perform a structured health check and produce a report covering:

1. **Cross-link completeness** — Are related articles linked to each other? List any missing links
   that should be added (e.g., security deposit article should link to move-out guide).

2. **Content gaps** — Are there topics that are mentioned but not fully covered? What important
   questions might a student have that the wiki doesn't answer?

3. **Inconsistencies** — Does any information contradict between articles (e.g., conflicting
   timelines, different advice on the same topic)?

4. **New article suggestions** — Based on the existing content, what 2–3 new articles would
   significantly improve the knowledge base? Give a title and 1-sentence rationale for each.

5. **Overall quality score** — Rate the knowledge base 1–10 for completeness, accuracy,
   and usefulness for international students. Justify your score in 2–3 sentences.

Be specific and actionable. Format your report clearly with headers and bullet points."""


def read_wiki_files() -> dict[str, str]:
    files = {}
    for f in sorted(WIKI_DIR.rglob("*.md")):
        files[str(f)] = f.read_text(encoding="utf-8")
    return files


def run_lint(wiki_files: dict[str, str]) -> str:
    client = anthropic.Anthropic()

    wiki_content = "\n\n".join(
        f"=== {path} ===\n{content}" for path, content in wiki_files.items()
    )

    print("  Calling Claude API for health check...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"=== KNOWLEDGE BASE TO REVIEW ===\n\n{wiki_content}",
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "type": "text",
                        "text": LINT_PROMPT,
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


def main():
    print("=== lint.py: Knowledge Base Health Check ===\n")

    wiki_files = read_wiki_files()
    if not wiki_files:
        print(f"No wiki files found in {WIKI_DIR}/. Run compile_wiki.py first.")
        sys.exit(1)

    print(f"Found {len(wiki_files)} wiki articles.\n")
    for path in wiki_files:
        print(f"  - {path}")
    print()

    report = run_lint(wiki_files)

    print("\n" + "=" * 60)
    print("HEALTH CHECK REPORT")
    print("=" * 60 + "\n")
    print(report)

    OUTPUTS_DIR.mkdir(exist_ok=True)
    report_path = OUTPUTS_DIR / "lint_report.md"
    report_path.write_text(f"# Knowledge Base Health Check Report\n\n{report}\n", encoding="utf-8")
    print(f"\n[Report saved to {report_path}]")


if __name__ == "__main__":
    main()
