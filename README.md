<div align="center">

# 🎓 Student Performance Predictor

### Predict exam scores using Machine Learning — powered by Flask & Scikit-learn

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML_Model-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 About The Project

**Student Performance Predictor** is a machine learning web application that predicts a student's exam score based on their study habits and academic behavior.

Enter details like study hours, attendance, sleep hours, and more — and the model instantly predicts your exam score along with a grade and personalized advice.

---

## ✨ Features

- 🔮 **Predicts exam score** out of 100 using a trained ML model
- 🏅 **Grade assignment** — A+, A, B, C, D, or F based on predicted score
- 💡 **Personalized advice** for each grade band
- ⚡ **Fast & lightweight** — built with Flask
- 🌐 **Clean web UI** accessible in any browser

---

## 🧠 How It Works

The model is trained on student data using **Linear Regression**. It takes 6 input features:

| Feature | Description |
|---|---|
| `study_hours` | Daily hours spent studying |
| `attendance` | Attendance percentage (0–100) |
| `previous_score` | Score in previous exam |
| `sleep_hours` | Average hours of sleep per night |
| `assignments_done` | Number of assignments completed |
| `tutoring_sessions` | Number of tutoring sessions attended |

The model then outputs a **predicted exam score** with grade and advice.

---

## 🗂️ Project Structure

```
student_performance_predictor/
│
├── app.py                  # Flask web application
├── train.py                # Model training script
├── model.pkl               # Pre-trained ML model
├── student_data.csv        # Training dataset
│
└── templates/
    └── index.html          # Frontend UI
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed.

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/KanekiAyush/Student_Performance_Predictor.git
cd student_performance_predictor
```

**2. Install dependencies**
```bash
pip install flask scikit-learn numpy pandas
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## 🔁 Retrain the Model (Optional)

If you want to retrain the model from scratch:

```bash
python train.py
```

This will print the model accuracy and regenerate `model.pkl`.

---

## 📊 Model Details

| Property | Value |
|---|---|
| Algorithm | Linear Regression |
| Library | Scikit-learn |
| Train/Test Split | 75% / 25% |
| Evaluation Metric | R² Score |

---

## 🏅 Grade Scale

| Score | Grade | Status |
|---|---|---|
| 90 – 100 | A+ | Outstanding |
| 80 – 89 | A | Excellent |
| 70 – 79 | B | Good |
| 60 – 69 | C | Average |
| 50 – 59 | D | Below Average |
| Below 50 | F | Failing |

---

## 🛠️ Tech Stack

- **Backend** — Python, Flask
- **ML Model** — Scikit-learn (Linear Regression)
- **Frontend** — HTML, CSS, JavaScript
- **Data** — Pandas, NumPy

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **[Ayush Thakare](https://github.com/KanekiAyush)**

⭐ Star this repo if you found it helpful!

</div>
