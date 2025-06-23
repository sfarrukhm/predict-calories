# 🔥 Calorie Prediction Microservice App

This project is a simple, interactive web application that predicts calories burned during exercise, based on user input as following:
 `age`, `weight`, `height`,`duration of exercise`, `heart rate`, and `current body temperature`.

It follows a **microservice-based architecture** using:
- **Streamlit** as the frontend UI
- **FastAPI** as the backend prediction API

---

## 🧠 What It Does

- Collects user details (like age, height, weight, duration of exercise, etc.) through a friendly web interface.
- Sends that data to a FastAPI microservice.
- Applies feature engineering and a trained machine learning model to predict calories burned.
- Returns the prediction to the frontend and displays it.

---
---

## 🚀 How to Run It Locally

Make sure you have Python 3.8+ installed. Then:

### 1. Clone the repo
```bash
git clone https://github.com/sfarrukhm/predict-calories.git
cd predict-calories
```
### 2. Install dependencies
Create and activate a virtual environment first:
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Then install dependencies
pip install -r requirements.txt
```
### 3. Start the FastAPI backend
```bash
cd predictor_service
uvicorn main:app --reload
```
This will start the API server at `http://localhost:8000`

### 4. Start the Streamlit frontend
```bash
cd frontend
streamlit run app.py
```
## 📚 Inspiration & Data Source

This project is based on the dataset provided in the [Kaggle Playground Series - Season 5, Episode 5](https://www.kaggle.com/competitions/playground-series-s5e5), which involves predicting calories burned during exercise.

The feature engineering and modeling techniques can be seen in following notebook:
> 📓 [KMeans Clustering-Based FE Improves CV & LB Scores](https://www.kaggle.com/code/sayyedfarrukhmehmood/kmeans-clustering-based-fe-improves-cv-lb-scores) 
