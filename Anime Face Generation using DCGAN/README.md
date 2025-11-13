# 🎨 Anime Face Generation using DCGAN

A deep-learning project focused on creating new anime-style face images by training a DCGAN (Deep Convolutional Generative Adversarial Network) model on an anime face dataset.

---

## 📌 Project Overview

This pipeline includes data loading and preprocessing, building a generator and discriminator network (DCGAN architecture), training adversarially, and generating new anime face images. The aim is to learn the underlying distribution of anime faces and generate realistic, novel images.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** PyTorch or TensorFlow/Keras, numpy, matplotlib, tqdm
* **Environment:** Jupyter Notebook / Google Colab / GPU

---

## 🔄 Workflow Summary

### 1. Data Collection & Pre-processing

* Dataset: Anime face images (e.g., cropped images resized to 64×64) ([Hackers Realm][1])
* Clean images, resize to fixed dimension, normalize pixel values to [-1, +1] range for tanh output of generator ([Hackers Realm][1])

### 2. DCGAN Architecture

* Generator: Takes latent noise vector z and upsamples via transposed convolutions + BatchNorm + ReLU → output RGB image with tanh activation. ([Hackers Realm][1])
* Discriminator: Receives image (real or fake) and outputs probability of real vs fake via convolution layers + LeakyReLU. ([Hackers Realm][1])
* Loss: Binary cross-entropy for both networks; alternating training of D and G. ([Sicilian][2])

### 3. Training

* Batch training for many epochs (e.g., 50+) until the generator starts producing visually plausible images. ([Hackers Realm][1])
* Monitor loss curves for generator & discriminator, and visualize generated images at intervals to track progress.

### 4. Generation & Inference

* After training, sample new noise vectors to generator to produce new anime face images.
* Post-process output (denormalize, convert to image) and save/display generated faces.

---

## 📁 Project Structure

```
Anime-Face-Generation/
│── data/
│── notebooks/
│── src/
│── models/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* The generator learns to mimic the training set distribution, gradually moving from noise to structured faces.
* Good results were obtained with image size ~64×64; higher resolution requires changes in network complexity. ([Sicilian][2])
* Normalization of input data and proper weight init (mean = 0, stddev = 0.02) are critical for stable GAN training. ([mindspore.cn][3])
* Despite strong visual results, GANs may still produce artifacts and perfect identity is not guaranteed (especially at lower resolutions).

---

## 🚀 Future Improvements

* Move to higher-resolution outputs (128×128, 256×256) using progressive growing GAN or StyleGAN.
* Introduce conditioning (e.g., hair colour, character emotion) to generate controlled variations.
* Deploy as a web interface where users can generate anime faces by choosing latent seeds or attributes.
* Use evaluation metrics like FID/IS to compare generated image quality and diversity quantitatively.
* Incorporate domain-specific datasets to generate anime faces with varied styles (e.g., chibi vs realistic anime).

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

[1]: https://www.hackersrealm.net/post/anime-face-generation-using-dcgan-python?utm_source=chatgpt.com "Anime Face Generation using DCGAN - Python - Hackers Realm"
[2]: https://srujana2505.github.io/projects/dcgan-on-anime-face/?utm_source=chatgpt.com "DCGAN on Anime Face - Sicilian"
[3]: https://www.mindspore.cn/tutorials/en/r2.4.0/generative/dcgan.html?utm_source=chatgpt.com "Generating Cartoon Head Portrait via DCGAN"

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
