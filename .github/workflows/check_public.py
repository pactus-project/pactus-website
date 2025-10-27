import os
import re
import sys

def find_unparsed_tags(root_folder: str):
    # Matches things like {{ ... }} or {{- ... -}}
    pattern = re.compile(r"{{.*?}}", re.DOTALL)
    found_issues = []

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if not filename.lower().endswith(('.html', '.xml', '.json', '.txt')):
                continue  # Skip non-text files

            full_path = os.path.join(dirpath, filename)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"⚠️ Skipping {full_path}: {e}")
                continue

            matches = pattern.findall(content)
            if matches:
                found_issues.append((full_path, matches))

    return found_issues


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_public_folder>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a valid directory.")
        sys.exit(1)

    issues = find_unparsed_tags(folder)
    if not issues:
        print("✅ No unparsed Hugo tags found.")
    else:
        print("❌ Found unparsed tags in the following files:\n")
        for file_path, matches in issues:
            print(f"{file_path}:")
            for match in matches:
                snippet = match.strip().replace("\n", " ")
                print(f"  → {snippet[:120]}{'...' if len(snippet) > 120 else ''}")
            print()
        sys.exit(2)
