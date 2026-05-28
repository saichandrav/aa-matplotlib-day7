# matplotlib_assignment.py

import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 170, 140, 200]

plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o', linestyle='--', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart

students = ['A', 'B', 'C', 'D', 'E']
marks = [78, 85, 90, 67, 88]

plt.figure(figsize=(6,4))
plt.bar(students, marks, color='green')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot
hours = [1, 2, 3, 4, 5, 6]
scores = [35, 45, 50, 60, 65, 80]

plt.figure(figsize=(6,4))
plt.scatter(hours, scores, color='red', s=100)
plt.title("Study Hours vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.show()

# 4. Histogram
data = np.random.randint(1, 100, 50)

plt.figure(figsize=(6,4))
plt.hist(data, bins=10, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


# 5. Pie Chart
languages = ['Python', 'Java', 'C++', 'JavaScript']
students_count = [40, 25, 20, 15]

plt.figure(figsize=(6,4))
plt.pie(students_count, labels=languages, autopct='%1.1f%%')
plt.title("Programming Language Popularity")
plt.show()