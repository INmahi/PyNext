#Day 1 mini project
##GPA Calculator
# Ishat Noor Mahi. 3006

marks = input("Enter marks: ")
#Check if the entered number is even a number, to prevent error
if marks.isnumeric() == True:
    marks = float(marks)
    if 80<=marks<=100:
        print("Grade Point: 4.0 | Letter Grade: A+")
    elif 70<= marks <80:
        print("Grade Point: 3.5 | Letter Grade: A")
    elif 60<= marks <70:
        print("Grade Point: 3.0 | Letter Grade: B")
    elif 50<= marks <60:
        print("Grade Point: 2.5 | Letter Grade: C")
    elif 40<= marks <50:
        print("Grade Point: 2.0 | Letter Grade: D")
    elif marks<40 and marks>=0: 
        print("Grade Point: 0.0 | Letter Grade: F")
    else:
        print("Invalid marks")
    
else:
    print("Please enter a valid number")
