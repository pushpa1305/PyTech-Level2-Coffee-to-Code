from model import load_and_train_model

def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter {subject} Score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Enter numeric value.")

def main():
    print("Training model using dataset...")
    model, accuracy = load_and_train_model("StudentsPerformance.csv")

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    while True:
        print("\n--- Pass/Fail Predictor ---")
        math = get_valid_score("Math")
        reading = get_valid_score("Reading")
        writing = get_valid_score("Writing")

        prediction = model.predict([[math, reading, writing]])[0]

        if prediction == 1:
            print("Predicted Result: PASS")
        else:
            print("Predicted Result: FAIL")

        cont = input("\nDo you want to predict again? (y/n): ").lower()
        if cont != 'y':
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()