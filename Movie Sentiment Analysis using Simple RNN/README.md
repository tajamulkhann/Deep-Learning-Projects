
# 🎬 Movie Sentiment Analysis Using Simple RNN

A deep-learning project focused on classifying movie reviews as positive or negative using a simple recurrent neural network (RNN) architecture.

---

## 📌 Project Overview

This project delivers a full pipeline: text data ingestion (movie reviews), preprocessing and tokenization, building an RNN model (e.g., SimpleRNN or LSTM variant), training and evaluation, and applying the model to predict sentiments. The objective is to enable sentiment classification of textual movie reviews with a compact model.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, TensorFlow/Keras or PyTorch, matplotlib, seaborn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection & Pre-processing

* Load movie-review dataset (e.g., IMDB) with fields such as review text and sentiment label.
* Clean the text: lowercase, remove HTML tags/punctuation, tokenize.
* Convert words to sequences using tokenizer or embedding (e.g., Keras Tokenizer).
* Pad sequences to fixed length (e.g., 200 words) for input to RNN.
* Split dataset into training and validation/test sets.

### 2. Feature Engineering & Model Preparation

* Create embedding layer (e.g., embedding dimension = 100) to convert word indices to vectors.
* Define RNN architecture:

  * Embedding layer
  * SimpleRNN layer (or LSTM/GRU)
  * Fully connected (Dense) layer with sigmoid activation for binary sentiment output.

  ```python
  model = Sequential()
  model.add(Embedding(input_dim=vocab_size, output_dim=50, input_length=max_len))
  model.add(SimpleRNN(units=64))
  model.add(Dense(1, activation='sigmoid'))
  ```
* Compile model with `binary_crossentropy` loss and `accuracy` metric.

### 3. Training & Validation

* Train the model for several epochs (e.g., 10-20), monitor training/validation accuracy and loss.
* Use callbacks such as early stopping or model checkpointing to avoid over-fitting.
* Visualise training and validation curves.

### 4. Evaluation & Prediction

* Evaluate model on test set: accuracy, precision, recall, F1-score, confusion matrix.
* Use model to predict sentiment on new review text and display result.

---

## 📁 Project Structure

```
Movie-Sentiment-Analysis-Simple-RNN/
│── data/
│   ├── train.csv
│   └── test.csv
│── notebooks/
│   └── sentiment_rnn.ipynb
│── src/
│   ├── preprocess.py
│   ├── model.py
│   └── train.py
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* RNNs effectively capture sequential dependencies in text and achieved good accuracy for binary sentiment classification.
* Using embedding and padding improved model readiness compared to raw text.
* Overfitting was mitigated via dropout or early stopping; validation accuracy approached training accuracy with good generalisation.
* For better performance, more advanced architectures (LSTM/GRU, bidirectional layers) or attention mechanisms were helpful.

---

## 🚀 Future Improvements

* Replace the SimpleRNN with **LSTM or Bidirectional LSTM/GRU** for improved contextual understanding.
* Expand dataset to multi-sentiment classes (multi-label) or multilingual reviews.
* Deploy as a web app or API where users can submit a movie review and receive sentiment feedback.
* Use interpretability tools (e.g., word-importance heatmaps) to show which words influenced classification.
* Combine with pretrained language models (e.g., BERT) for transfer-learning and higher accuracy.

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
