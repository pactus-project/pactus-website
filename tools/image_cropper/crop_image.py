from PIL import Image
import argparse


def crop_image(image_path:str, output_path:str, ratio:float, direction:str):
    image = Image.open(image_path)
    width, height = image.size
    target_ratio = ratio

    if width / height > target_ratio:
        # Crop width
        new_width = int(height * target_ratio)
        if direction == "left":
            left, upper, right, lower = 0, 0, new_width, height
        elif direction == "right":
            left, upper, right, lower = width - new_width, 0, width, height
        else:  # center (default)
            left = (width - new_width) // 2
            right = left + new_width
            upper, lower = 0, height
    else:
        # Crop height
        new_height = int(width / target_ratio)
        if direction == "top":
            left, upper, right, lower = 0, 0, width, new_height
        elif direction == "down":
            left, upper, right, lower = 0, height - new_height, width, height
        else:  # center (default)
            upper = (height - new_height) // 2
            lower = upper + new_height
            left, right = 0, width

    cropped_image = image.crop((left, upper, right, lower))
    cropped_image.save(output_path)
    print(f"Image saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trim an image to a specific aspect ratio."
    )
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save the trimmed image")
    parser.add_argument(
        "--ratio",
        default="16/9",
        help="Aspect ratio to crop to (default: 16/9)",
    )
    parser.add_argument(
        "--direction",
        choices=["top", "down", "left", "right", "center"],
        default="center",
        help="Direction to trim from",
    )
    args = parser.parse_args()

    if len(vars(args)) < 3:
        parser.print_help()
        exit(1)

    target_ratio = 0
    try:
        target_width, target_height = map(float, args.ratio.split("/"))
        target_ratio = target_width / target_height
    except ValueError:
        print("Error: Invalid aspect ratio format. Use 'width/height' (e.g., 16/9, 4/3).")
        exit(1)
    crop_image(args.image_path, args.output_path, target_ratio, args.direction)
