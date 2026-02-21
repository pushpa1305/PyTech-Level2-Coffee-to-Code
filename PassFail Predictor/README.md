# Student Pass/Fail Prediction Project

## Problem Chosen

The goal of this project is to predict whether a student will **Pass** or **Fail** based on their academic performance.
A student is considered:

* **Pass** if the average of Math, Reading, and Writing scores is ≥ 40
* **Fail** if the average score is < 40

A Logistic Regression model is trained on the dataset to perform this classification.

## Dataset Source

The dataset used is **StudentsPerformance.csv**, which contains student scores in Math, Reading, and Writing.
Source: Kaggle (Students Performance in Exams dataset)

## How to Run the Project

1. Download the dataset `StudentsPerformance.csv` and place it in the project folder.
2. Install the required libraries:

   ```
   pip install pandas scikit-learn
   ```
3. Run the program using:

   ```
   py main.py
   ```
4. Enter Math, Reading, and Writing scores when prompted to get the Pass/Fail prediction.
