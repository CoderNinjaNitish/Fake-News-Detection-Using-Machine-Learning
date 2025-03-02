# 📰 Fake News Detection

## 📌 Project Overview
This project aims to build a **Fake News Detection System** using **Machine Learning**. The system analyzes news articles and predicts whether a given news article is **real** or **fake** based on the text content.

## 🏗️ Tech Stack Used
- **Python** (Main Programming Language)
- **Flask** (For Web Framework)
- **Machine Learning Models** (Logistic Regression)
- **NLTK** (For Natural Language Processing)
- **TfidfVectorizer** (For Text Feature Extraction)
- **Joblib** (For Model Serialization)
- **Pandas & NumPy** (For Data Handling)

## 📂 Folder Structure
```
D:/fake news detection/
│── fake-news/           # Dataset Folder
│   ├── train.csv        # Training Dataset
│   ├── test.csv         # Testing Dataset
│   ├── submit.csv       # Submission File
│── app.py               # Flask Application
│── model.ipynb          # Jupyter Notebook for Model Training
│── model_fake_news.joblib     # Saved ML Model
│── vectorizer_fake_news.joblib  # Saved TF-IDF Vectorizer
│── templates/
│   ├── index.html       # Frontend Webpage
│── static/
│   ├── style.css        # Styling
│── README.md            # Project Documentation
```

## 📊 Dataset Details
The dataset contains the following columns:
- `id` - Unique Identifier
- `title` - News Title
- `author` - Author Name
- `text` - Full News Content
- `label` - (0 = Real News, 1 = Fake News)

## 🚀 Steps to Run the Project
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model (If Not Saved)
Run `model.ipynb` to train the model and save it using:
```python
import joblib
joblib.dump(model, "model_fake_news.joblib")
joblib.dump(vectorizer, "vectorizer_fake_news.joblib")
```

### 3️⃣ Run the Flask App
```bash
python app.py
```
Now, open **http://127.0.0.1:5000/** in the browser to use the web app.

## 🖥️ Web App Features
✔ Enter a news article and get **Real** or **Fake** prediction.  
✔ Simple and Interactive UI.  
✔ Machine Learning-based detection with high accuracy.

## 🎯 Future Improvements
- Adding **Deep Learning Models** like LSTMs.
- Using **BERT-based NLP models** for better accuracy.
- Creating a **REST API** for real-time fake news detection.

## 🤝 Contributing
Feel free to contribute! Fork the repo, make changes, and submit a pull request.

## 📜 License
This project is open-source and available under the **MIT License**.

---

🎉 **Enjoy Fake News Detection!**

