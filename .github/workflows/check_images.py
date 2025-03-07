### This is temporary script to check the old images are 16:9 ratio.
### We can delete it later.

import os
import sys
import markdown
import sys
import toml
from PIL import Image
from pathlib import Path


def extract_toml_header(md_file: str):
    """Extracts the TOML header from the Markdown file."""
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check that the file starts with the expected TOML front matter delimiter
    if lines[0].strip() != "+++":
        print(f"Error: Invalid header format in '{md_file}'")
        sys.exit(1)

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


def check_image_file_names():
    for root, _, files in os.walk("./content/blog"):
        for file in files:
            md_file = root + "/" + file
            header = extract_toml_header(md_file)
            image = header.get("image", "")

            if image == "" or image == "/images/pactus-blog-post-default.jpg":
                continue

            folder = Path(md_file).stem
            image_file = "./assets/blog/" + folder + "/" + image
            with Image.open(image_file) as img:
                # Check aspect ratio (16:9)
                width, height = img.size
                aspect_ratio = round(width / height, 2)
                expected_ratio = round(16 / 9, 2)

                if aspect_ratio != expected_ratio:
                    print(
                        f" ⚠️ Image is NOT 16:9 (Actual: {width}x{height}, Ratio: {aspect_ratio}, Expected Ratio {expected_ratio}) - {file}"
                    )
                    sys.exit(1)

if __name__ == "__main__":
    check_image_file_names()
