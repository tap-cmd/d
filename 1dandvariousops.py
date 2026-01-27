import pandas as pd

print("Create a Series: \n")
marks = pd.Series([85, 90, 78, 92, 88])
print(marks , "\n")

print("Create Series with Custom Index: \n ")
students = pd.Series([85, 90, 78],
                      index=["Alice", "Bob", "Charlie"])
print(students, "\n")

print("====== OPERATIONS ON SERIES ====== \n")
print("Accessing Elements: \n " )
print(students["Alice"])

print("Arithmetic Operation: \n")

print(students + 5, "\n")


print("Statistical Operations:")
print("Maximum:", students.max())
print("Minimum:", students.min())
print("Average:", students.mean(),"\n")


print("Filtering Data: \n")
print(students[students > 80])


print("Updating Value: \n")
students["Bob"] = 95
print(students)

print("Check Data type:", students.dtype, "\n")

print("Convert Series to list: \n", students.tolist())

