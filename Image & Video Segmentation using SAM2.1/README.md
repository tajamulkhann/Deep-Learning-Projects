# 🎥 Image & Video Segmentation using SAM2.1

A deep-learning project focused on leveraging the SAM 2.1 (Segment Anything Model 2.1) foundation model to perform promptable segmentation on both images and videos. It uses prompt-based object segmentation (points, boxes, masks) and supports temporal propagation for video sequences.

---

## 📌 Project Overview

This project implements a full pipeline:

* Downloading/pre-processing image & video datasets.
* Applying SAM 2.1 to segment objects based on user prompts.
* Handling both static image segmentation and video segmentation with temporal consistency.
* Evaluating segmentation quality, analysing mask propagation in video, and refining interaction loops.
  The goal is to enable flexible segmentation of any object (zero-shot) in images or videos and to build tools around it for real-world applications.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** PyTorch, torchvision, OpenCV, numpy, matplotlib
* **Model:** SAM 2.1 from Meta AI Research / FAIR. ([GitHub][1])
* **Environment:** Jupyter Notebook / Google Colab / GPU (CUDA)

---

## 🔄 Workflow Summary

### 1. Data Collection & Pre-processing

* Collect images and video files earmarked for segmentation tasks.
* Extract video frames (JPEG), preprocess images/videos (resize, normalise).
* For video: prepare prompt frames, object IDs, and initialise SAM 2.1 inference state. ([Roboflow Blog][2])

### 2. Model Setup & Prompting

* Load SAM 2.1 checkpoint and configuration.
* For image: use `SAM2ImagePredictor` or equivalent API. ([Hugging Face][3])
* For video: use `SAM2VideoPredictor`, initialise inference state, add point/box prompts, propagate masks. ([Roboflow Blog][2])

### 3. Segmentation & Mask Propagation

* In image mode: apply selected prompts (points, boxes) to generate segmentation mask(s).
* In video mode: input prompt on an initial frame, then propagate predictions frame-by-frame while object IDs persist, using memory attention for temporal consistency. ([GitHub][1])
* Visualise segmentation output overlayed on input frames for qualitative assessment.

### 4. Evaluation & Insights

* For images: evaluate segmentation masks for correctness and prompt-responsiveness.
* For videos: monitor mask propagation fidelity, object ID tracking accuracy, temporal coherence, occlusion handling.
* Analyse and summarise segmentation performance (qualitative & quantitative).
* Extract application insights: e.g., how zero-shot segmentation opens up new workflows in annotation or editing.

---

## 📁 Project Structure

```
Image-&-Video-Segmentation-SAM2.1/
│── data/
│── notebooks/
│── src/
│── models/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* SAM 2.1 enables promptable segmentation in both images and videos with strong zero-shot generalisation. ([Medium][4])
* Temporal memory and propagation in video mode allow consistent object tracking across frames, reducing manual intervention.
* Use of prompts (points, boxes) significantly influences segmentation outcome — careful prompting improves precision.
* For video tasks, handling occlusion & object reappearance remains a challenge; memory-mechanism design is crucial.
* The segmentation pipeline can accelerate annotation workflows, visual editing, and content-production tasks by automating masks.

---

## 🚀 Future Improvements

* Integrate segmentation output into downstream pipelines (e.g., object tracking, video editing, AR applications).
* Extend prompt types and interaction (e.g., negative prompts, mask-based prompts) for fine-grained control.
* Deploy as web- or mobile-app allowing upload of image/video + interactive prompt GUI.
* Incorporate multi-object tracking in video with dynamic object addition/removal during propagation.
* Monitor and mitigate edge-cases (thin objects, fast motion, heavy occlusion) where segmentation quality decays.

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

---

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
