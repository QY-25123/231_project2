"""
ask.py — Step 3 of the knowledge base workflow.

Ask a question against the compiled wiki. Streams the answer to stdout
and saves it as a markdown file in outputs/.

Usage:
    python ask.py "What happens if my landlord doesn't return my deposit?"
    python ask.py "How do I set up electricity in a new apartment?"
"""

import anthropic
import re
import sys
from pathlib import Path

WIKI_DIR = Path("wiki")
OUTPUTS_DIR = Path("outputs")

SYSTEM_PROMPT = """You are a knowledgeable assistant helping international students navigate
U.S. apartment rentals. Answer questions based on the provided knowledge base.

Guidelines:
- Be concise and practical. Students need actionable advice.
- When relevant, cite which wiki article covers the topic in more detail.
- Use numbered steps for processes, bullet points for lists.
- Flag legal rights or important warnings clearly.
- If the knowledge base doesn't cover something, say so rather than guessing."""


def read_wiki_files() -> dict[str, str]:
    files = {}
    for f in sorted(WIKI_DIR.rglob("*.md")):
        files[str(f)] = f.read_text(encoding="utf-8")
    return files


def build_wiki_context(files: dict[str, str]) -> str:
    sections = []
    for path, content in files.items():
        sections.append(f"=== {path} ===\n{content}")
    return "\n\n".join(sections)


def ask_question(question: str, wiki_files: dict[str, str]) -> str:
    client = anthropic.Anthropic()
    wiki_context = build_wiki_context(wiki_files)

    full_answer = []
    print(f"Answer:\n")

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"=== KNOWLEDGE BASE ===\n{wiki_context}",
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "type": "text",
                        "text": f"Question: {question}",
                    },
                ],
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_answer.append(text)

    print("\n")
    return "".join(full_answer)


def save_output(question: str, answer: str) -> Path:
    OUTPUTS_DIR.mkdir(exist_ok=True)
    safe_name = re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:60]
    output_path = OUTPUTS_DIR / f"{safe_name}.md"
    output_path.write_text(
        f"# Q: {question}\n\n{answer}\n",
        encoding="utf-8",
    )
    return output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python ask.py \"your question here\"")
        print('\nExample: python ask.py "What is normal wear and tear?"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    wiki_files = read_wiki_files()
    if not wiki_files:
        print(f"No wiki files found in {WIKI_DIR}/. Run compile_wiki.py first.")
        sys.exit(1)

    print(f"Q: {question}\n")
    print(f"(Knowledge base: {len(wiki_files)} articles)\n")
    print("-" * 60)

    answer = ask_question(question, wiki_files)

    output_path = save_output(question, answer)
    print(f"[Saved to {output_path}]")


if __name__ == "__main__":
    main()
