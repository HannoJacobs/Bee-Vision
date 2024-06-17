
bees_dataset_4 - v1 2024-05-03 4:07pm
==============================

This dataset was exported via roboflow.com on May 3, 2024 at 2:07 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2797 images.
Bees-type-RsHi-Ewql-Llz6 are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random shear of between -33° to +33° horizontally and -23° to +23° vertically
* Random brigthness adjustment of between -29 and +29 percent
* Salt and pepper noise was applied to 10 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random Gaussian blur of between 0 and 1.3 pixels
* Salt and pepper noise was applied to 0.1 percent of pixels


