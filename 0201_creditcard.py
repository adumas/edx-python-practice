#!/usr/bin/python


"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

      # Test Case 1:
      balance = 42
      annualInterestRate = 0.2
      monthlyPaymentRate = 0.04

      # Result Your Code Should Generate Below:
      Remaining balance: 31.38

"""


def minPaymentYear(balance=42, annualInterestRate=0.2, monthlyPaymentRate=0.04):
    n_months = 12
    currentMonth = 1
    monthlyRate = annualInterestRate / 12.

    while currentMonth <= n_months:
        if currentMonth > 0:
            balance += balance * monthlyRate

        minPayment = balance * monthlyPaymentRate
        balance -= minPayment

        print("Month {} Remaining balance: {:.2f}".format(currentMonth, balance))

        currentMonth += 1

    return round(balance, 2)


print(minPaymentYear())
