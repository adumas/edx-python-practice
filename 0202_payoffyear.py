#!/usr/bin/python

"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180
"""


def yearBalance(balance=42, annualInterestRate=0.2, monthlyPayment=10):
    n_months = 12
    currentMonth = 1
    monthlyRate = annualInterestRate / 12.

    while currentMonth <= n_months:
        balance -= monthlyPayment
        if currentMonth > 0:
            balance += balance * monthlyRate
        currentMonth += 1

    return round(balance, 2)


def payoff(balance=3329, annualInterestRate=0.2):
    # lambda to get closest in 10's
    def roundten((x)): return round(x / 10.) * 10

    # half balance
    tryPayment = 10
    remain = 1
    while remain > 0:
        tryPayment += 10
        remain = yearBalance(balance, annualInterestRate, tryPayment)
        # print tryPayment, remain

    # print remain
    return tryPayment


test = [3329, 4773, 3926]
for ta in test:
    print(ta, payoff(ta))
