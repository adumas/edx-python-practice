#!/usr/bin/python

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
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
    # half balance
    lo = balance / 12.
    hi = (balance * (1 + 0.2 / 12)**12) / 12.
    remain = 1
    while not remain == 0:
        tryPayment = (lo + hi) / 2.
        remain = yearBalance(balance, annualInterestRate, tryPayment)
        if remain > 0:
            lo = tryPayment
        else:
            hi = tryPayment
        # print tryPayment, remain

    # print remain
    return tryPayment


print payoff(320000)

print payoff(999999, 0.18)
