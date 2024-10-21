import os
import sys

def check_image_file_names(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.png', '.gif')):
                if '_' in file:
                    print(f"Image file {os.path.join(root, file)} should bot have '_' in  its path.")
                    sys.exit(1)

            if file.lower().endswith(('.jpeg', '.bmp', '.tiff', '.webp')):
                print(f"Image file {os.path.join(root, file)} is not a JPG, PNG or GIF.")
                sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_images.py <root_directory>")
        sys.exit(1)

    root_directory = sys.argv[1]
    check_image_file_names(root_directory)
