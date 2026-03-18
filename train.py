import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle

# Load dataset
df = pd.read_csv("student_data.csv")

# Select input features
X = df[[
"study_hours",
"attendance",
"previous_score",
"sleep_hours",
"assignments_done",
"tutoring_sessions"
]]

# Target output
y = df["exam_score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Accuracy score
accuracy = r2_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy*100,2), "%")

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")