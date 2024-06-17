# Model Card For Bee-Vision
==============================

Last updated: June 2024

This model is a computer vision object detection model that is used to identify and classify different bees according to their species. It works on the following classes:

- Allodapula
- Apis-mellifera-scutellata
- Braunsapis
- Lasioglossum
- Meliponula
- Seladonia
- Thyreus
- Xylocopa

## Table of Contents

- [Model details](#model-details)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
- [Technical Specifications](#technical-specifications)
- [Training Details](#training-details)
- [Evaluation](#evaluation)
- [Environmental Impact](#environmental-impact)
- [How to Get Started with the Model](#how-to-get-started-with-the-model)
- [Citations](#citations)

## Model Details
------------

Provide a longer summary of what this model is. Include details such as the input and output of the model.  

### Model Description

- **Developed by:**
   - Hanno Jacobs - u17000042@tuks.co.za
   - Yasekwa Dutywa - u23825848@tuks.co.za

- **Model type:**
   -  YOLOv8-nano Pytorch computer vision object detection model
- **Language(s) (NLP):**
   - N/A
- **License:**
   - AGPL-3.0 license

### Model Source

- **Repository:** [ultralytics](https://github.com/ultralytics/ultralytics)

### Model Type

CNN computer vision object detection model for identification and classification of bee species from images.

### Model version

Version 1.0

## Intended Uses
------------

### Primary uses

This model is made to be used to identify the differetnt species of bees from images.

## Bias, Risks, and Limitations
------------

No possible harm or bias can be derived from using the model

## Technical Specifications 
-----------

### Model Architecture

Model architecture is based on a CNN model from Ultralytics called YOLOv8-nano

### Compute Infrasture

- **Hardware:**

The model can be trained on any PC that supports CPU training and works best when trained on a NVidia GPU that is powered by CUDA. The model can be used for inference on any CPU based platform that supports Python 3. This can also be sped up by running on an NVidia GPU that is powered by CUDA.

- **Software:**

This model requires Python 3 and the packages in the requirements.txt file to run.

## Training Details 
-----------

### Training data

This model's training data is split up into train, val and test datasets with images and labels in each of the folders. The labels must be saved in the YOLO format.

### Training Procedure/Process

The model can be retrained using the [src/YOLOv8_train.py](src/YOLOv8_train.py) script in the repo. This training can be adjusted by changing the [src/train_yaml_paths/dataset_1_train.yaml](src/train_yaml_paths/dataset_1_train.yaml) file in the repo to the desired path and classes.

### Training Hyperparameters

There is no need to change any of the hyperparameters when training. The hyperparams are fine as default, however the batch size can be increased if training on a very powerful device.

## Evaluation
-----------

### Testing Data

The model is automatically evaluated on the test dataset in the dataset folder if trained by the training script provided.

### Factors

There are no mitigating factors to consider.

### Metrics

The following metrics are automatically generated when training with the train script in the repo

- F1-confidence curve
- Recall-confidence curve
- Precision-confidence curve
- Precision-recall curve
- Confusion matrix
- Train metrics:
   - train/val box loss
   - train/val class loss
   - train/val dfl loss
   - precision
   - recall
   - mAP50
   - mAP50-95

### Results

## Environmental Impact
-----------

- **Hardware Type:**

   - NVidia RTX2060

- **Hours used:**

   - 3 hours for Nano model
   - 9 hours for X model

- **Cloud Provider:**

   - Private infrastructure

- **Compute Region:**

   - N/A

- **Carbon Emitted:**

   - 0.25 kg CO2 eq for Nano model
   - 0.75 kg CO2 eq for Nano model

## How to Get Started with the Model
------------

### Install python 3.10

```sh
sudo apt update && sudo apt upgrade -y && sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 && sudo apt install software-properties-common -y && sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.10 && sudo apt-get install python3.10 python3.10-venv python3-pip && python3.10 --version
```

### Create a virtual environment

Create the virtual environment and then install the requirements

```sh
python3.10 -m venv .venv && source .venv/bin/activate && python3 -m pip install -U -r requirements.txt
```

If any of the above requirements fail to install and you just want to visualise the model you can run this command only and it should work

```sh
python3 -m pip install matplotlib streamlit tensorflow pillow ultralytics opencv-python
```

### Using the Streamlit inferencing tool

To use the model to inference on any bees image that you want run this command. It will open your browser window with the app ready for you to drop an image to infer on.

```sh
source .venv/bin/activate && .venv/bin/streamlit run visualization/visualise_inference.py
```

### Using the Streamlit augmentation visualisation tool

To look at what the different augmentation parameters do run this command. It will open your browser with the app ready for you to test the augmentation settings

```sh
source .venv/bin/activate && .venv/bin/streamlit run visualization/visualise_augmentation.py
```

### Inference with the model in Python code

```py
from ultralytics import YOLO
import cv2

model_path = "<your model.pt path>"
frame_path = "<image path to inference on>"

frame = cv2.imread(frame_path)
model = YOLO(model_path)
yolo_detections = model.predict(frame, iou=0.7, agnostic_nms=True, conf=0.25)
r = yolo_detections[0]
cv2.imshow("Frame", r.plot()) # show the plot
cv2.waitKey(0)
```

## Citations
-----------

Bee Species Identification by Hanno Jacobs and Yasekwa Dutywa 2024

BibTeX

``` 

@misc{BeeVision2024,
   title={Bee-Vision},
   author={Jacobs, Hanno (and Dutywa, Yasekwa)},
   year={2024},
   url={https://github.com/up-mitc-ds/808-2024-bees_team}
}

```

APA 

```
Author {Jacobs, H and Yasekwa, D}.(2024). Bee-Vision. https://github.com/up-mitc-ds/808-2024-bees_team

```

## Author Details
----------

* Written by : Hanno Jacobs and Yasekwa Dutywa
* Contact details :
   - Hanno Jacobs - u17000042@tuks.co.za
   - Yasekwa Dutywa - u23825848@tuks.co.za

