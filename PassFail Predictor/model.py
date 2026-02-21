import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def load_and_train_model(csv_file):
    # Load dataset
    df = pd.read_csv(csv_file)

    # Create target column (Pass >= 40 else Fail)
    df["average_score"] = (
        df["math score"] + df["reading score"] + df["writing score"]
    ) / 3

    df["result"] = df["average_score"].apply(lambda x: 1 if x >= 40 else 0)

    # Features and target
    X = df[["math score", "reading score", "writing score"]]
    y = df["result"]

    # Train-test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy