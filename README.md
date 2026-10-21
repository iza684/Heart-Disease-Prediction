<div align="center">

# ❤️ Heart Disease Risk Predictor

**A machine learning web app that predicts high or low risk of heart disease from 11 basic health inputs.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://your-app-name.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-KNN-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

### 🔗 [Try the Live App]([https://your-app-name.streamlit.app](https://heart-disease-prediction-akazcmdasfu6munjt2aljs.streamlit.app/))

<img width="1361" height="657" alt="Image" src="https://github.com/user-attachments/assets/4180d962-d0d4-4fb3-9426-15a7409b3500" />

</div>

---

## 📌 About

Heart disease is one of the leading causes of death worldwide, and early screening matters. This project takes a few simple health details (age, blood pressure, cholesterol, ECG, etc.) and predicts whether the person is at **high risk** or **low risk** using a **K-Nearest Neighbors (KNN)** model.

It is an end-to-end project: data cleaning, model training, saving the model, and deploying it as an interactive web app.

---

## ✨ Features

- 🎨 Modern dark UI with custom CSS (gradient background, glass-style inputs, themed sliders)
- 🧾 11 easy inputs: sliders, dropdowns and number fields
- ⚡ Instant prediction: ✅ Low Risk or ⚠️ High Risk
- 🔁 Same preprocessing as training (one-hot encoding + scaling), so predictions stay consistent
- ☁️ Deployed on Streamlit Community Cloud

---

## 🧾 Input Features

| Feature | Description | Values |
|---|---|---|
| Age | Age of the patient | 18 – 100 |
| Sex | Gender | M / F |
| Chest Pain Type | Type of chest pain | ATA, NAP, TA, ASY |
| Resting BP | Resting blood pressure (mm Hg) | 80 – 200 |
| Cholesterol | Serum cholesterol (mg/dL) | 100 – 600 |
| Fasting BS | Fasting blood sugar > 120 mg/dL | 0 / 1 |
| Resting ECG | Resting ECG result | Normal, ST, LVH |
| Max HR | Maximum heart rate achieved | 60 – 220 |
| Exercise Angina | Exercise-induced angina | Y / N |
| Oldpeak | ST depression caused by exercise | 0.0 – 6.0 |
| ST Slope | Slope of the peak exercise ST segment | UP, Flat, Down |

---

## 🧠 How It Works

```
User Input  →  One-Hot Encoding  →  Column Alignment  →  StandardScaler  →  KNN Model  →  Risk Result
```

1. The user fills in the health details in the app.
2. Categorical inputs are converted into one-hot columns (e.g. `ChestPainType_ATA`).
3. Missing columns are filled with `0` and reordered to match `columns.pkl`, so the input has exactly the shape the model was trained on.
4. Values are scaled with the saved `StandardScaler`.
5. The KNN model predicts: `0` = Low Risk, `1` = High Risk.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas, NumPy | Data handling |
| scikit-learn | KNN model and scaling |
| Joblib | Saving and loading model files |
| Streamlit | Web app and UI |
| HTML / CSS | Custom styling |

---

## 📂 Project Structure

```
heart-disease-prediction/
└── heart_disease/
    └── Heart Disease Prediction app/
        ├── app.py              # Streamlit app
        ├── KNN_heart.pkl       # Trained KNN model
        ├── scaler.pkl          # Fitted StandardScaler
        ├── columns.pkl         # Expected feature columns
        ├── requirements.txt    # Dependencies
        └── .streamlit/
            └── config.toml     # Theme settings
```

---

## ▶️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/heart-disease-prediction.git

# 2. Go to the app folder
cd "heart-disease-prediction/heart_disease/Heart Disease Prediction app"

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the app
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 📊 Model Details

| | |
|---|---|
| **Algorithm** | K-Nearest Neighbors (KNN) |
| **Dataset** | Heart Failure Prediction Dataset (Kaggle) |
| **Preprocessing** | One-hot encoding, StandardScaler |
| **Accuracy** | 89% |



---

## ⚠️ Limitations

- Trained on a small dataset, so it may not generalise to all populations.
- KNN is sensitive to scaling and to the choice of `k`.
- Only meant to demonstrate an ML workflow.

---



## ⚠️ Disclaimer

This project is for **educational purposes only** and is **not a medical diagnosis tool**. Always consult a qualified doctor for health concerns.

---

## 👤 Author

**Izaan Ansari**
B.Tech Information Technology Student | Aspiring Data Analyst

[LinkedIn](https://www.linkedin.com/in/izaan-ansari/) • [GitHub]([https://github.com/your-username](https://github.com/iza684))

---

<div align="center">

⭐ If you liked this project, give it a star!

</div>
