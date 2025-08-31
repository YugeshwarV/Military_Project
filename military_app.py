import streamlit as st
import cv2
import tempfile
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Load YOLOv8 trained model
model = YOLO("C:/Users/yuges/Desktop/Data Science/Final Project/Final/best.pt") 
model.to("cpu")

# Class mapping
class_names = {
    0: "Camouflage_Soldier",
    1: "Military_Tank",
    2: "Soldier",
    3: "Aircrafts",
    4: "Warship"
}

# Define threat classes
threat_classes = {0}   # Only Camouflage_Soldier


def classify_threat(cls_id):
    return "Threat" if cls_id in threat_classes else "Non-Threat"


def process_frame(frame):
    results = model(frame, conf=0.5)

    for r in results:
        boxes = r.boxes.xyxy.cpu().numpy()
        confs = r.boxes.conf.cpu().numpy()
        clss = r.boxes.cls.cpu().numpy().astype(int)

        for box, conf, cls in zip(boxes, confs, clss):
            x1, y1, x2, y2 = map(int, box)
            label = class_names[cls]
            status = classify_threat(cls)

            color = (0, 0, 255) if status == "Threat" else (0, 255, 0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} ({status}) {conf:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame


# Streamlit UI
st.title("Military Object Detection & Threat Classification")
st.write("Upload an **image** or a **video** to detect and classify threats.")

uploaded_file = st.file_uploader("Upload Image or Video", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

if uploaded_file:
    file_type = uploaded_file.type

    # ------------------ IMAGE ------------------
    if file_type.startswith("image"):
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        processed_img = process_frame(img_array)

        st.image(processed_img, caption="Processed Image", channels="BGR")

    # ------------------ VIDEO ------------------
    elif file_type.startswith("video"):
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        output_frames = []

        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            processed_frame = process_frame(frame)
            output_frames.append(processed_frame)

            # Display each frame live
            stframe.image(processed_frame, channels="BGR")

        cap.release()

        st.success("Video Processing Completed")
