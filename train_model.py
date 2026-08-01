import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import pickle


# Load dataset
data = pd.read_csv("dataset.csv")

# Separate input and output
X = data["review"]
y = data["sentiment"]


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Convert text into numbers
vectorizer = TfidfVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)


# Create model
model = LogisticRegression()


# Train model
model.fit(X_train, y_train)


# Check accuracy
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)


# Save model
pickle.dump(model, open("model.pkl", "wb"))

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully")