#  Sentiment Analysis Web Application

A Machine Learning based web application that analyzes user reviews and predicts whether the sentiment is **Positive** or **Negative**. This project is developed using **Python, Flask, Scikit-learn, HTML, and CSS**. It uses the **TF-IDF Vectorizer** and **Logistic Regression** algorithm to classify text sentiments accurately.

---

## Features

-  Predicts Positive and Negative Sentiments
-  Interactive Web Interface using Flask
-  Machine Learning Model (Logistic Regression)
-  TF-IDF Text Vectorization
-  Fast and Accurate Predictions
-  Clean and Responsive User Interface

---

##  Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Scikit-learn
- Pandas
- Pickle

---

## Project Structure

```text
Sentiment_Analysis/
│── app.py
│── train_model.py
│── dataset.csv
│── model.pkl
│── vectorizer.pkl
│── templates/
│    └── index.html
│── static/
│    └── style.css
│── README.md
```1. Install the required libraries.
2. Train the model using `train_model.py`.
3. Run the Flask application using `app.py`.
4. Open `http://127.0.0.1:5000` in your browser.
5. Enter a review and click **Analyze** to view the sentiment. 

--- 

## Sample Prediction 

**Input:** 

> I really loved this product. It is amazing. 

**Prediction:** 

> Positive 

**Input:** 

> This product is terrible. I hate it. 

**Prediction:** 

> Negative 

--- 

## Future Improvements 

- Neutral Sentiment Detection
- Deep Learning (LSTM/BERT)
- Charts & Analytics Dashboard
- User Login System

---

## 🚀 How to Run
