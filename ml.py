import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow,joblib
import mlflow.sklearn

data = {
    "age": [25, 35, 45, 23, 52, 40, 29, 60, 31, 48],
    "salary": [30000, 50000, 70000, 28000, 90000,
               65000, 35000, 100000, 45000, 75000],
    "experience": [1, 5, 10, 1, 15, 8, 3, 20, 5, 12],
    "churn": [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

features = df[['age', 'salary', 'experience']]
target = df['churn']

with mlflow.start_run():
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    print("Training set size:", x_train)

    print("Test set size:", x_test)

    model = RandomForestClassifier(n_estimators=100, random_state=42,max_depth=5)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    print(classification_report(y_test, y_pred))

    mlflow.log_param("n_estimators",100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "random_forest_model")

    joblib.dump(model,"randomforest_model.pkl")