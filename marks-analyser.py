import numpy as np
marks = np.array([
    [78, 85, 90],
    [88, 76, 92],
    [67, 70, 60],
    [90, 95, 94],
    [72, 80, 75]
])

print("Student Marks:\n", marks)

student_avg = np.mean(marks, axis=1)
print("\nAverage marks of each student:", student_avg)

# Average marks of each subject
subject_avg = np.mean(marks, axis=0)
print("Average marks of each subject:", subject_avg)

# Highest and lowest marks
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))

# Class average
class_avg = np.mean(marks)
print("Class average marks:", class_avg)
