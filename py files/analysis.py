import pandas as pd

# Load the dataset
data = pd.read_csv("data/student-por.csv", sep=";")


# Preview data
print("First 5 rows:")
print(data.head())

# Dataset info
print("\nDataset Info:")
print(data.info())

# Missing values
print("\nMissing values:")
print(data.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Average grades
average_grades = data[['G1', 'G2', 'G3']].mean()
print("\nAverage Grades:")
print(average_grades)

# Study time vs final grade
studytime_performance = data.groupby('studytime')['G3'].mean()
print("\nAverage Final Grade by Study Time:")
print(studytime_performance)

# Absences vs final grade
absences_performance = data.groupby('absences')['G3'].mean()
print("\nAverage Final Grade by Absences:")
print(absences_performance)
