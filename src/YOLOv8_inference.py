from ultralytics import YOLO
import cv2


if __name__ == "__main__":
    model_path = "runs/detect/train/weights/best.pt"
    frame_path = "Dataset/Dataset_tools/mosaic_creator/mosaic_1.jpg"

    frame = cv2.imread(frame_path)
    model = YOLO(model_path)
    # yolo_detections = model.predict(frame, conf=0.25)
    yolo_detections = model.predict(frame, iou=0.7, agnostic_nms=True, conf=0.25)
    r = yolo_detections[0]
    cv2.imshow("Frame", r.plot())
    cv2.waitKey(0)
