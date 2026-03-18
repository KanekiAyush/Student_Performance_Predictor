from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# load trained model
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html", trained=True)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    study_hours = float(data["study_hours"])
    attendance = float(data["attendance"])
    previous_score = float(data["previous_score"])
    sleep_hours = float(data["sleep_hours"])
    assignments_done = float(data["assignments_done"])
    tutoring_sessions = float(data["tutoring_sessions"])

    features = np.array([[study_hours, attendance, previous_score,
                          sleep_hours, assignments_done, tutoring_sessions]])

    prediction = model.predict(features)[0]

    score = round(float(prediction), 2)

    # limit score between 0 and 100
    score = max(0, min(score, 100))

    # Grade logic
    if score >= 90:
        grade = "A+"
        status = "Outstanding"
        advice = "Excellent performance. Maintain your study routine."
    elif score >= 80:
        grade = "A"
        status = "Excellent"
        advice = "Great job. Keep practicing regularly."
    elif score >= 70:
        grade = "B"
        status = "Good"
        advice = "Good performance. Increase study hours for higher score."
    elif score >= 60:
        grade = "C"
        status = "Average"
        advice = "Focus more on assignments and revision."
    elif score >= 50:
        grade = "D"
        status = "Below Average"
        advice = "Increase study time and attend tutoring sessions."
    else:
        grade = "F"
        status = "Failing"
        advice = "You need significant improvement. Study consistently."

    return jsonify({
        "success": True,
        "score": score,
        "grade": grade,
        "status": status,
        "advice": advice
    })

if __name__ == "__main__":
    app.run(debug=True)