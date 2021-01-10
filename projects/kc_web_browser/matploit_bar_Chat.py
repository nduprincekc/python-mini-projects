import matplotlib.pyplot as plt

grades = ['A', 'B', 'C', 'D', 'E', 'F']
students_count = [20, 30, 10, 5, 8, 2]

plt.bar(grades, students_count, color=['green', 'gray', 'yellow', 'gray', 'gray', 'red'])
plt.title('Grades Bar Plot for Biology Class')
plt.xlabel('Grade')
plt.ylabel('Num Students')
plt.show()



plt.title('Grades Bar Plot for Biology Class')
plt.xlabel('Num Students')
plt.ylabel('Grade')
plt.barh(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
