names = []
marks = []

for i in range(20):
    n = input(f"Enter name for student {i+1}: ")
    m = float(input(f"Enter marks for student {i+1}: "))
    names.append(n)
    marks.append(m)

for i in range(20):
    n = names[i]
    m = marks[i]

    if m >= 90:
        grade = "Distinction"
    elif m >= 75:
        grade = "First Division"
    elif m >= 60:
        grade = "Second Division"
    elif m >= 35:
        grade = "Third Division"
    else:
        grade = "Fail"

    print(f"Student {i+1}: Name = {n}, Marks = {m}, Grade = {grade}")

print("\nAll names:", names)
print("All marks:", marks)