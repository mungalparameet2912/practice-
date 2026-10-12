percentage = float(input("Enter the percentage of a student: "))

if percentage <100 and percentage >80:
    print("Very good result") 
elif percentage < 80 and percentage > 61:
    print("Good result")
elif percentage < 61 and percentage > 41:
    print("Average result")
else: 
    print("Bad result")