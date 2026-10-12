eng_marks = int(input("Enter the marks of English: "))
math_marks = int(input("Enter the marks of Maths: "))

# if both are more than 80,print A grade
if eng_marks > 80 and math_marks > 80:
    print("A Grade")
# if any one are more than 80,print B grade
elif eng_marks >80 or math_marks > 80:
    print("B Grade")
# if both are less than 80,print C grade
else:
    print("C Grade")