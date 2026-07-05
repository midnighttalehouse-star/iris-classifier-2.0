import os
import argparse
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def main():
    parser = argparse.ArgumentParser(description="Train an Iris Decision Tree model")
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--random-state", type=int, default=42)

    args = parser.parse_args()

    # Load dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=args.test_size,
        random_state=args.random_state,
    )

    # Train model
    model = DecisionTreeClassifier(random_state=args.random_state)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=iris.target_names,
        yticklabels=iris.target_names,
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.tight_layout()

    plt.savefig("outputs/confusion_matrix.png")
    plt.close()

    # Save model
    joblib.dump(model, "outputs/model.joblib")

    print("Confusion matrix saved to outputs/confusion_matrix.png")
    print("Model saved to outputs/model.joblib")


if __name__ == "__main__":
    main()
