# 📬 Spam Mail Detector 🛡️  
A machine learning-powered web application that identifies spam emails using an ensemble of classification models.

---

## 🔍 Overview

**Spam Mail Detector** is a web-based tool that detects whether an email is **spam** or **not spam**. It uses three different machine learning classifiers and determines the result by **majority voting** among them.

---

## 🚀 Live Demo

🔗 **Try it here:** [Spam Mail Detector](https://spam-mail-detector.vercel.app/)

---

## 🧠 How It Works

The app uses the following classifiers:
- 📈 **Logistic Regression**
- 🧮 **Naive Bayes**
- 📏 **Support Vector Machine (SVM)**

Each model independently predicts the email category, and the final result is based on the **majority prediction**.

---

## 🛠️ Technologies Used

### Frontend:
- [React.js](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)

### Backend:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Gunicorn](https://gunicorn.org/)
- [Render](https://render.com/) – for backend deployment

---

## 🧪 Model Training

- **Dataset**: `emails.csv` with labeled spam and ham emails
- **Preprocessing**: Emails are cleaned and transformed using `TfidfVectorizer`
- **Training**:
  - Three models: Logistic Regression, Naive Bayes, and SVM
  - Models are saved with `pickle`
- **Prediction**:
  - Models are loaded on the backend
  - Predictions are made for input email text
  - Final result is the majority vote among the three
