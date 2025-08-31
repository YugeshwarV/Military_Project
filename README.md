# Military_Project
# Military Soldier Safety & Threat Detection  

This project leverages **YOLOv8 (Large variant)** and **Computer Vision** to detect and classify military objects from images and videos. It enhances soldier safety by identifying **threats (Camouflage Soldiers)** while distinguishing them from **non-threat entities** like tanks, warships, aircraft, and regular soldiers.  

---

## Problem Statement  
In modern combat environments, **situational awareness** is critical. Soldiers face threats from camouflaged enemy soldiers, vehicles, and aircrafts. Manual monitoring is error-prone and slow.  
This system automates the process of **detecting, classifying, and tagging threats** in real time using computer vision.  

---

## Model Performance  
| Class              | Images | Instances | Precision (P) | Recall (R) | mAP@50 | mAP@50-95 |  
|--------------------|--------|-----------|---------------|------------|--------|-----------|  
| **All (avg)**      | 2450   | 4269      | 0.88          | 0.814      | 0.871  | 0.64      |  
| Camouflage Soldier | 385    | 510       | 0.776         | 0.792      | 0.82   | 0.474     |  
| Military Tank      | 938    | 1787      | 0.852         | 0.812      | 0.865  | 0.59      |  
| Soldier            | 420    | 745       | 0.888         | 0.687      | 0.791  | 0.543     |  
| Aircrafts          | 594    | 1063      | 0.922         | 0.806      | 0.885  | 0.706     |  
| Warship            | 150    | 164       | 0.96          | 0.97       | 0.993  | 0.886     |  

**Key Results:**  
- Overall **mAP@50 = 0.871** (87.1%).  
- **Threat detection accuracy:** Camouflage Soldier detected reliably.  
- Warships & Aircrafts achieved **highest accuracy (>90%)**.  

---

## Features  
- Detects 5 classes:  
  - **Threat:** Camouflage Soldier  
  - **Non-Threat:** Military Tank, Soldier, Aircrafts, Warship  
- **Real-time detection** on images & videos.  
- **Color-coded bounding boxes:**  
  - Red → Threat  
  - Green → Non-Threat  
- Interactive **Streamlit Web App**.  

---

## Project Structure  
```
├── military_app.py                       # Streamlit app for detection & threat classification
├── MilitaryProjectNB-EDA and Preprocessing.ipynb   # Data analysis & preprocessing
├── modeltr.ipynb                         # YOLOv8 model training notebook
├── Military Soldier Safety.pdf           # Formal project documentation
├── best.pt                               # Trained YOLOv8 model (not included in repo)
├── requirements.txt                      # Project dependencies
```

---

## Installation  

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/military-soldier-safety.git
   cd military-soldier-safety
   ```

2. Create environment & install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Place your trained YOLO model (`best.pt`) in the root folder.  

---

## Running the App  

```bash
streamlit run military_app.py
```

Then open the provided **local URL** in your browser.  

---

## Usage  

- **Upload an Image** → processed with bounding boxes & labels.  
- **Upload a Video** → real-time detection frame by frame.  
- **Threat = Camouflage Soldier** → highlighted in **Red**.  
- **Non-Threat (Tank, Soldier, Aircraft, Warship)** → highlighted in **Green**.  

---

## Business Use Cases  
- Military Surveillance & Reconnaissance  
- Border Security & Intrusion Detection  
- Soldier Safety Alert Systems  
- Disaster Response & Rescue Ops  
- Training & Simulation for Defense  

---

## Built by 
# Yugeshwar V  
