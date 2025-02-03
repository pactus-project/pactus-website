import markdown
import sys
import toml
from pathlib import Path


def load_template(template_file: str):
    """Reads the HTML email template from a file."""
    if not Path(template_file).is_file():
        print(f"Error: Template file '{template_file}' not found.")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        return f.read()


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


def convert_markdown_to_html(template_file: str, md_file: str, output_html: str):
    """Converts a Markdown file to an HTML email using a template."""
    if not Path(md_file).is_file():
        print(f"Error: File '{md_file}' not found.")
        sys.exit(1)

    # Extract TOML header
    header = extract_toml_header(md_file)

    # Check if title or description is missing or empty
    title = header.get('title', '').strip()
    description = header.get('description', '').strip()
    image = header.get('image', '').strip()

    folder = Path(md_file).stem
    newsletter_image = f"../assets/blog/{folder}/{image}"

    if not title:
        print("Error: 'title' is missing in the TOML header.")
        sys.exit(1)

    if not description:
        print("Error: 'description' is missing in the TOML header.")
        sys.exit(1)

    # Read the Markdown file and remove the header section.
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split off the header: remove everything from the start to the second +++ marker.
    # This splits the file into 3 parts: empty, header, and markdown content.
    parts = content.split("+++", 2)
    if len(parts) < 3:
        print("Error: Markdown content not found after header.")
        sys.exit(1)
    md_content = parts[2].strip()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    description = description.replace("\n", " ")

    # Load template and inject content
    template = load_template(template_file)
    html = template.replace("{{.title}}", title)
    html = html.replace("{{.preheader}}", description)
    html = html.replace("{{.content}}", html_content)
    html = html.replace("{{.newsletter_image}}", newsletter_image)

    # Save output file
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)

    print("")
    print(f"Email Sender Name: Pactus Newsletter")
    print(f"Email Subject:     {title}")
    print(f"Email Preheader:   {description}")
    print(f"Email HTML:        {output_html}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 md_to_email.py newsletter.md")
        sys.exit(1)

    convert_markdown_to_html(
        md_file=sys.argv[1],
        output_html="email.html",
        template_file="newsletter.tmpl"
    )
