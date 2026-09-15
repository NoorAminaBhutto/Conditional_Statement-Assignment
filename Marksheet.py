name = input("Enter name: ")
roll = input("Enter roll no: ")

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if per >= 80 and per <= 100:
    grade = "A+"
elif per >= 70:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
else:
    grade = "F"

if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40:
    result = "Fail"
else:
    if per >= 40:
        result = "Pass"
    else:
        result = "Fail"

print("\n--- Student Marksheet ---")
print("Name:", name)
print("Roll No:", roll)
print("Marks:", m1, m2, m3, m4, m5)
print("Total:", total)
print("Percentage:", per)
print("Grade:", grade)
print("Result:", result)