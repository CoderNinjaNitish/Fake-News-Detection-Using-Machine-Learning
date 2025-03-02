from flask import Flask, request, jsonify, render_template
import joblib

# ✅ Load trained model aur vectorizer
model = joblib.load("model_fake_news.joblib")
vectorizer = joblib.load("vectorizer_fake_news.joblib")

# ✅ Flask app banayein
app = Flask(__name__)

# 📌 Home Route (HTML Form)
@app.route("/")
def home():
    return render_template("index.html")  # Ensure index.html is in 'templates' folder

# 🚀 Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    news_text = request.form["news"]  # Form se news text lein
    transformed_text = vectorizer.transform([news_text])  # Text ko number me convert karein
    prediction = model.predict(transformed_text)  # Model se prediction karein

    result = "REAL News ✅" if prediction[0] == 0 else "FAKE News ❌"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
