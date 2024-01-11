salary=int(input("Salary:"))
age=int(input("Age:"))
if(salary>=20000 or age<=25):
    loan=int(input("Required Loan Amount:"))
    if(loan>50000):
        print("Maximum Loan amount is 50000")
    else:
        print("You are Eligible for Loan")

else:
    print("Your not Eligible")
