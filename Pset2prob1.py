# Paste your code into this box
totalPaid = 0

for i in range(1, 13):
    minMonthlyPayment = round((balance * monthlyPaymentRate), 2)
    totalPaid += minMonthlyPayment
    remainingBalance = balance - minMonthlyPayment
    balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
balance = round(balance,2)
print("Remaining balance: " + str(balance))