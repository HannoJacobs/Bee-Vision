"""
Resource page:
https://docs.ultralytics.com/modes/train/#key-features-of-train-mode
"""

from ultralytics import YOLO

training_yaml_file_path = "train.yaml"  # NB: always use .yaml never .yml
model = YOLO("yolov8n.pt")  # Here we select the model to train based on
model.train(
    data=training_yaml_file_path,
    epochs=200,
    patience=200,
    imgsz=640,
)
