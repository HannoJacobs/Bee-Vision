"""
Resource page:
https://docs.ultralytics.com/modes/train/#key-features-of-train-mode


run command:
cd /Users/hannojacobs/Documents/2_Uni/808_bees_official_github/ && source .venv/bin/activate && python3 src/YOLOv8_train.py

"""

import os
from ultralytics import YOLO

yaml_paths = "src/train_yaml_paths"
dataset_name = "dataset_5v1_train"
training_yaml_file_path = os.path.join(yaml_paths, dataset_name + ".yaml")
model = YOLO("models/yolov8n.pt")  # Here we select the model to train based on

for i in range(0, 10):
    model.train(
        data=training_yaml_file_path,
        epochs=1000,
        patience=200,
        # epochs=1,
        # patience=1,
        imgsz=640,
        device=0,  # cuda training
        batch=32,
        project="runs/detect/augmentation_test_1",
        name=f"{dataset_name}_{i}",
        dropout=0.025 * i,
        shear=5.0 * i,
        mixup=0.03 * i,
        copy_paste=0.04 * i,
        auto_augment="randaugment",
        crop_fraction=0.04 * i,
        cls=2.0,
    )
