from PIL import Image
import numpy as np
from pathlib import Path


def create_mosaic(image_files, output_file, rows, cols):
    # Load images
    images = [Image.open(file) for file in image_files]

    # Determine the max dimensions
    max_width = max_height = min_width = min_height = None

    # Determine min and max dimensions to maintain aspect ratio
    for i in images:
        if max_width is None or i.size[0] > max_width:
            max_width = i.size[0]
        if max_height is None or i.size[1] > max_height:
            max_height = i.size[1]
        if min_width is None or i.size[0] < min_width:
            min_width = i.size[0]
        if min_height is None or i.size[1] < min_height:
            min_height = i.size[1]

    # The size each image needs to be rescaled to
    target_width = max_width // cols
    target_height = max_height // rows

    # Create the mosaic image
    mosaic = Image.new("RGB", (max_width, max_height))

    # Resize and paste images into the mosaic
    for idx, image in enumerate(images):
        # Calculate the scaling factor
        scaling_factor = min(
            target_width / image.size[0], target_height / image.size[1]
        )

        # Compute the new size to maintain aspect ratio
        new_width = int(image.size[0] * scaling_factor)
        new_height = int(image.size[1] * scaling_factor)

        # Resize the image using the scaling factor
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Calculate position (top left corner of where the image will be pasted)
        row = idx // cols
        col = idx % cols
        left = col * target_width + (target_width - new_width) // 2
        upper = row * target_height + (target_height - new_height) // 2

        # Paste the resized image into the mosaic
        mosaic.paste(resized_image, (left, upper))

    # Save the mosaic
    mosaic.save(output_file)
    return mosaic


# Define the directory path where to look for images
directory_path = Path("mosaic_creator/input_images")

# Specify the images to combine
image_paths = (
    list(directory_path.glob("*.jpg"))
    + list(directory_path.glob("*.jpeg"))
    + list(directory_path.glob("*.JPG"))
    + list(directory_path.glob("*.png"))
)

# Specify the output file name
output_file = "mosaic_creator/mosaic_1.jpg"

# Define the number of rows and columns in the mosaic
rows = cols = int(np.ceil(np.sqrt(len(image_paths))))

# Create and save the mosaic
create_mosaic(image_paths, output_file, rows, cols)
