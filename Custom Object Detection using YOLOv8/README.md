# 🎯 Custom Object Detection using YOLOv8

A deep-learning project focused on detecting custom object classes by fine-tuning the YOLOv8 model on a tailored dataset and deploying the resulting detector for real-world inference.

---

## 📌 Project Overview

This project delivers a full-cycle pipeline: preparing a custom object-detection dataset (images + annotations), adapting YOLOv8 for new classes, training and validating, and deploying for inference. The goal is to build a high-performance detector for domain-specific objects that weren’t available in standard datasets.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** `ultralytics` (YOLOv8), OpenCV, pandas, numpy, matplotlib
* **Environment:** Jupyter Notebook / Google Colab / GPU
* **Model:** YOLOv8 (pre-trained on COCO, fine-tuned on custom data) ([LearnOpenCV][1])

---

## 🔄 Workflow Summary

### 1. Data Preparation

* Collect images covering all custom classes and varied contexts.
* Annotate images using bounding boxes and save in YOLO format (one `.txt` per image: `class x_center y_center width height` with normalized coords).
* Create a YAML dataset config file:

  ```yaml
  train: path/to/train/images
  val:   path/to/val/images
  nc:    <number_of_classes>
  names: ['class1','class2',…]
  ```

  ([Medium][2])

---

### 2. Model Setup & Training

* Install YOLOv8 via pip:

  ```bash
  pip install ultralytics
  ```

  ([Roboflow Blog][3])
* Use CLI or Python API:

  ```bash
  yolo task=detect mode=train model=yolov8s.pt data=custom.yaml imgsz=640 epochs=50 name=custom_detector
  ```
* Monitor metrics like mAP@0.5:0.95, loss curves. ([LearnOpenCV][1])

---

### 3. Evaluation & Inference

* Validate the trained model:

  ```bash
  yolo task=detect mode=val model=runs/detect/name/weights/best.pt data=custom.yaml
  ```
* Run inference on images/videos:

  ```python
  from ultralytics import YOLO
  model = YOLO('best.pt')
  results = model.predict(source='test.jpg', save=True, conf=0.25)
  ```

  ([Medium][2])
* Analyse output boxes, classes and confidence scores.

---

### 4. Deployment

* Export to ONNX/TensorRT/CoreML/Edge format if required:

  ```python
  model.export(format='onnx')
  ```

  ([DigitalOcean][4])
* Integrate into an app, video pipeline or monitoring system.

---

## 📁 Project Structure

```
Custom-Object-Detection-YOLOv8/
│── data/
│   ├── train/
│   ├── val/
│   └── custom.yaml
│── notebooks/
│── src/
│── runs/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Fine-tuned YOLOv8 on custom classes achieved high detection accuracy and speed in target domains.
* Even small-sized models (like `yolov8s`) performed robustly when dataset and annotations were well-curated. ([LearnOpenCV][1])
* Proper dataset splitting (train/val), annotation format, and hyper-parameter tuning (img size, epochs, batch) were critical for performance.
* Exported models supported real-time inference on edge devices when optimized.

---

## 🚀 Future Improvements

* Augment dataset with more diverse contexts (lighting, angles, occlusion) to boost robustness.
* Try larger YOLOv8 versions (`yolov8m`, `yolov8l`) for higher accuracy if compute allows.
* Incorporate tracking (YOLOv8+Track) for video-based object monitoring.
* Set up CI/CD pipeline for model retraining with new data and deploy updates automatically.
* Build interactive UI for annotating new data and incremental training.

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.datascientist/" target="_blank">
<img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://topmate.io/tajamulkhan" target="_blank">
<img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0MCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white">
</a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f">
<img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>
<a href="https://t.me/tajamul_khan">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://substack.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719">
</a>
<a href="https://www.kaggle.com/tajamulkhan">
<img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
</a>
<a href="https://github.com/tajamulkhann">
<img src="https://img.shields.io/badge/Github-12100E?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://medium.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">
</a>
<a href="https://www.youtube.com">
<img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</a>
</div>
