# Image Cropper

## Overview

This script allows you to crop an image to a specific aspect ratio while providing an option to specify the cropping direction.

## Requirements
- Python 3.x
- `Pillow` library (Install using `pip install pillow`)

## Usage
```sh
python3 image_cropper.py <input_image> <output_image> [--ratio <aspect_ratio>] [--direction <crop_direction>]
```

### Arguments
- `<input_image>`: Path to the input image.
- `<output_image>`: Path to save the cropped image.
- `--ratio`: Optional. Aspect ratio to crop to (default: 16/9). Example: `4/3`.
- `--direction`: Optional. Specifies the cropping direction (`top`, `down`, `left`, `right`, `center`). Default is `center`.

### Examples
Crop an image to 16:9 from the center:
```sh
python3 image_cropper.py input.jpg output.jpg
```

Crop an image to 4:3 from the top:
```sh
python3 image_cropper.py input.jpg output.jpg --ratio 4/3 --direction top
```
