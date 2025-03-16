import os
import git
import sys
import toml
from pathlib import Path
from PIL import Image

BASE_BRANCH = "main"

repo = git.Repo()
head_commit = repo.head.commit  # Latest commit on PR branch

# Find the merge base (common ancestor) between PR branch and main
base_commit = repo.merge_base(head_commit, f"origin/{BASE_BRANCH}")[0]

# Get all changed files in PR commits
changed_files = set()
for commit in repo.iter_commits(f"{base_commit.hexsha}..{head_commit.hexsha}"):
    changed_files.update(commit.stats.files.keys())

print(f"Checking {len(changed_files)} files modified in this PR...\n")

def check_images(file):
    try:
        # Reopen for further checks
        with Image.open(file) as img:
            if '_' in file:
                print(f"❌ Image file should bot have '_' in  its path: {file}")
                sys.exit(1)

            else:
                print(f" ✅ Image OK: {file}")

    except Exception as e:
        print(f" ❌ Corrupt image: {file} - {e}")
        sys.exit(1)


def extract_toml_header(md_file: str):
    """Extracts the TOML header from the Markdown file."""
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check that the file starts with the expected TOML front matter delimiter
    if lines[0].strip() != "+++":
        return None

    # Extract lines between the +++ markers
    header_lines = []
    for line in lines[1:]:
        if line.strip() == "+++":
            break
        header_lines.append(line)

    header_content = "\n".join(header_lines)
    try:
        header = toml.loads(header_content)
    except Exception as e:
        print(f"Error parsing TOML: {e}")
        sys.exit(1)

    return header

def check_markdown(file):
    header = extract_toml_header(file)
    if header == None:
        print(f" 🔹 Skipping {file} (no TOML header)")
        return

    image = header.get("image", "")
    if image == "" or image == "/images/pactus-blog-post-default.jpg":
        print(f" 🔹 Skipping {file} (no cover image)")
        return

    folder = Path(file).stem
    image_file = "./assets/blog/" + folder + "/" + image
    with Image.open(image_file) as img:
        # Check aspect ratio (16:9)
        width, height = img.size
        aspect_ratio = round(width / height, 2)
        expected_ratio = round(16 / 9, 2)

        if aspect_ratio != expected_ratio:
            print(f" ❌ Cover image is NOT 16:9 (Actual: {width}x{height}, Ratio: {aspect_ratio}, Expected Ratio {expected_ratio}) - {file}")
            sys.exit(1)

    print(f" ✅ Markdown OK: {file}")

# Process each file based on type
for file in changed_files:
    if not os.path.exists(file):
        print(f" 🔹 Skipping {file} (deleted)")
        continue

    if file.lower().endswith((".png", ".jpg", ".gif")):
        check_images(file)
    elif file.lower().endswith(('.jpeg', '.bmp', '.tiff', '.webp')):
        print(f" ❌ Image file {file} is not a JPG, PNG or GIF.")
        sys.exit(1)
    elif file.lower().endswith(".md"):
        check_markdown(file)
    else:
        print(f" 🔹 Skipping {file}")

print("\nCheck completed!")
