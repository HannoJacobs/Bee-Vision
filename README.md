# MIT808_bees_EDA

## What this repo does

This repo is used for the exploration of Bee image data and some preliminary model's analysis and performance.

## Folder structure

Folders:
1. google_scraped_dataset
- This is the dataset that was downloaded by using the dataset scraper tool
- This tool has been used to download 100 images of each of the types of bees

2. google-images-scraper-tool
- This is the tools that is used to download images of bees from the internet

3. images
- These are images of the bees types that are downloaded by the "google-images-scraper-tool" as a test

4. mosaic_creator
- This is a tool that is used to merge multiple images of bees into a single image.
- This is helpful for testing if multiple bees can be identified at a time in a single image's inference

5. runs
- This is the file that is created when a YOLOv8 model is trained on a custom dataset
- It creates the new model yolov8.pt file as well as images that display the various metrics that track the training process

6. src (Python code src files)
- This contains Python files that are used to train the model and test it for inferencing on images

7. `<root of the repo>`
- YOLO_world.ipynb - This is a Python notebook file that shows the results of inferencing on the mosaic image of different bee types with the zero-shot YOLO-World model
- YOLOv8_inference.ipynb - This is a Python notebook file that shows the results of inferencing on the mosaic image of different bee types using the custom trained YOLOv8n.pt model that was trained on the web scraped bee images

## Model efficacy demonstrated


## Usage


