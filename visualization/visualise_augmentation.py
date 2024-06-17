"""
run app:
.venv/bin/streamlit run visualization/visualise_augmentation.py
http://127.0.0.1:8501

This code is used to show the various levels and options for augmentation that can and are
used in the dataset before and during the training process
"""

import streamlit as st
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore


def load_image(image_path):
    return cv2.cvtColor(cv2.imread(str(image_path)), cv2.COLOR_BGR2RGB)


def plot_images(image_files, num_images=5):
    fig, axes = plt.subplots(1, num_images, figsize=(20, 20))
    for i, image_path in enumerate(image_files[:num_images]):
        image = load_image(image_path)
        axes[i].imshow(image)
        axes[i].axis("off")
        axes[i].set_title(image_path.stem)
    st.pyplot(fig)


def main():
    base_dir = Path("visualization/viz_images")
    image_files = list(base_dir.glob("*.png"))

    st.title("Bee Image Visualization and Augmentation")
    st.header("Original Images")
    num_images = st.slider("Number of images to display", 1, 8, 8)
    plot_images(image_files, num_images)

    st.header("Augmented Images")
    image_path = st.selectbox("Select an image to augment", image_files)
    image = load_image(image_path)
    image = np.expand_dims(image, 0)

    st.subheader("Augmentation Settings")
    rotation_range = st.slider("Rotation Range", 0, 45, 40)
    width_shift_range = st.slider("Width Shift Range", 0.0, 0.5, 0.2)
    height_shift_range = st.slider("Height Shift Range", 0.0, 0.5, 0.2)
    shear_range = st.slider("Shear Range", 0.0, 3.0, 0.2)
    zoom_range = st.slider("Zoom Range", 0.0, 0.5, 0.2)
    brightness_range = st.slider("Brightness Range", 0.0, 1.0, (0.8, 1.2))
    channel_shift_range = st.slider("Channel Shift Range", 0, 100, 50)

    datagen = ImageDataGenerator(
        rotation_range=rotation_range,
        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
        shear_range=shear_range,
        zoom_range=zoom_range,
        horizontal_flip=True,
        fill_mode="nearest",
        brightness_range=brightness_range,
        channel_shift_range=channel_shift_range,
    )

    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    for i, batch in enumerate(datagen.flow(image, batch_size=1)):
        axes[i].imshow(batch[0].astype("uint8"))
        axes[i].axis("off")
        if i == 4:
            break
    st.pyplot(fig)


if __name__ == "__main__":
    main()
