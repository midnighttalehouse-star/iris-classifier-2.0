# 🌸 Iris Classifier – Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---
## 📌 Overview

This project is a complete **end-to-end Machine Learning pipeline** built using the classic **Iris dataset**.

It demonstrates how a real-world ML workflow works:
- Data loading
- Training a model
- Evaluating performance
- Saving trained models
- Visualizing results

The model used is a **Decision Tree Classifier**, trained using `scikit-learn`.

---

## 🎯 Objective

To classify iris flowers into three species:
- 🌸 Setosa  
- 🌿 Versicolor  
- 🌺 Virginica  

based on:
- Sepal length
- Sepal width
- Petal length
- Petal width

---

## 🧠 Tech Stack

- Python 🐍
- Scikit-learn 🤖
- Matplotlib 📊
- Seaborn 🎨
- Jupyter Notebook 📓
- Joblib 💾

---

## 📁 Project Structure

```

iris-classifier-2.0/
│
├── data/
├── notebooks/
│   └── iris_model.ipynb
│
├── src/
│   └── train.py
│
├── outputs/
│   ├── confusion_matrix.png
│   └── model.joblib
│
├── tests/
│   └── test_train.py
│
├── requirements.txt
├── README.md
└── LICENSE

````

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/midnighttalehouse-star/iris-classifier-2.0.git
cd iris-classifier-2.0
````

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Run training script

```bash
python src/train.py --test-size 0.2 --random-state 42
```

---

## 📊 Model Performance

* Accuracy: ~95% – 100%
* Algorithm: Decision Tree Classifier
* Dataset: Iris (150 samples)

---

## 📉 Confusion Matrix

The model performance is visualized using a confusion matrix:

```
outputs/confusion_matrix.png
```

---

## 🧪 Testing

Run unit tests using:

```bash
pytest
```

Expected output:

```
1 passed
```

---

## 💡 Key Learnings

* End-to-end ML pipeline structure
* Train/test splitting
* Model evaluation techniques
* Overfitting vs generalization
* Saving models for reuse

---

## 📦 Future Improvements

* Add Random Forest / SVM models
* Deploy using Flask or FastAPI
* Build interactive web UI
* Add feature scaling & tuning
* Cross-validation improvements

---

## 👨‍💻 Author

**Saddam Hussain**
AI / ML Learner & Developer
GitHub: [https://github.com/midnighttalehouse-star](https://github.com/midnighttalehouse-star)