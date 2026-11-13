# Stage 2: find unchanged lines and collect unmatched line numbers.

from difflib import SequenceMatcher


def unix_diff(old_lines: list[str], new_lines: list[str]) -> dict:
    # Compare lines exactly; return matches and unmatched 1-based numbers.
    # Pass normalized lines from Stage 1 when using the full pipeline.
    result = {"matches": [], "unmatched_old": [], "unmatched_new": []}
    matcher = SequenceMatcher(None, old_lines, new_lines, autojunk=False)

    for tag, i, j, a, b in matcher.get_opcodes():
        if tag == "equal":
            result["matches"].extend(zip(range(i + 1, j + 1), range(a + 1, b + 1)))
        else:
            result["unmatched_old"].extend(range(i + 1, j + 1))
            result["unmatched_new"].extend(range(a + 1, b + 1))

    return result


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Find unchanged lines and collect unmatched line numbers."
    )
    parser.add_argument("old_file", type=Path)
    parser.add_argument("new_file", type=Path)
    args = parser.parse_args()

    try:
        old_lines = args.old_file.read_text(encoding="utf-8").splitlines()
        new_lines = args.new_file.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"Error: {error}\n")

    result = unix_diff(old_lines, new_lines)
    for old_number, new_number in result["matches"]:
        print(f"{old_number}-{new_number}")
    print("Unmatched old:", result["unmatched_old"])
    print("Unmatched new:", result["unmatched_new"])
