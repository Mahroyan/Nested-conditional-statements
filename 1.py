medical_cause=input("did you have a medical cause 'Y' or 'N'")
atten = int(input("Enter the attendence of the student: "))

if medical_cause == 'Y':
    print("You are allowed")
else:
    if atten>= 75:
        print("Allowed")
    else:
        print("Not allowed")