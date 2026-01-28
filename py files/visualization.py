import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/student-por.csv", sep=';')

# Set style
sns.set(style="whitegrid")

# -----------------------------
# 1. Average Grades Bar Chart
# -----------------------------
average_grades = data[['G1', 'G2', 'G3']].mean()

plt.figure()
average_grades.plot(kind='bar')
plt.title("Average Student Grades")
plt.xlabel("Assessment")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.savefig("outputs/average_grade.png")
plt.close()


# -----------------------------
# 2. Study Time vs Final Grade
# -----------------------------
plt.figure()
sns.boxplot(x='studytime', y='G3', data=data)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig("outputs/studytime_finalgrade.png")
plt.close()

# -----------------------------
# 3. Absences vs Final Grade
# -----------------------------
plt.figure()
sns.scatterplot(x='absences', y='G3', data=data)
plt.title("Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Grade")
plt.tight_layout()
plt.savefig("outputs/absences.png")
plt.close()
