income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
# Both conditions must be True because of 'and'
if income > 30000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")