"""
run app:
.venv/bin/streamlit run visualization/visualise_inference.py
http://127.0.0.1:8501
"""

import streamlit as sl
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

MODEL_PATH = "models/aug_test_1_train_1.pt"


def infer_and_plot(model_path, image, conf_threshold):
    model = YOLO(model_path)
    yolo_detections = model.predict(
        image,
        iou=0.7,
        agnostic_nms=True,
        conf=conf_threshold,
    )
    result_image = yolo_detections[0].plot()
    return result_image


if __name__ == "__main__":
    sl.title("Bee Species Detector")
    conf_threshold = sl.slider("Confidence threshold:", 0.0, 1.0, 0.25, 0.01)
    uploaded_images = sl.file_uploader(
        "Choose up to 8 images...",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    if uploaded_images:
        uploaded_images = uploaded_images[:8]  # Limit to 8 images

        for uploaded_image in uploaded_images:
            decoded_image = cv2.imdecode(
                np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8),
                cv2.IMREAD_COLOR,
            )
            images_with_plot = cv2.cvtColor(
                infer_and_plot(MODEL_PATH, decoded_image, conf_threshold),
                cv2.COLOR_BGR2RGB,
            )
            sl.image(Image.fromarray(images_with_plot), use_column_width=True)
