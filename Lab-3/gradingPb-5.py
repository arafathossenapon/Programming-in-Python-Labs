x = float(input("enter marks (out of 100): "))

if x<0 or x>100:
    print("Invalid marks.")
elif x>=90:
    print("Grade: A")
elif x>=80:
    print("Grade: B")
elif x>=70:
    print("Grade: C")
elif x>=60:
    print("Grade: D")
else:
    print("Grade: F")