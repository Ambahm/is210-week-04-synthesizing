#!usr/bin/env python
# -*- coding: utf-8 -*-

""" COMPOUND INTEREST CALCULATOR """

# decimal class for interest rate
import decimal

# QUAL_CHECK = ['Y', 'y', 'No', 'n']      # Qulaification variable

NAME = raw_input('Please Enter Your Name: ')
PRINCIPAL = int(raw_input('\nEnter the amount borrowed: '))
LOAN_TIME = int(raw_input('\nFor How many years loan is borrowed: '))
PREQUALIFY = raw_input('\nAre you prequalifed for the loan? (Y/N) ').lower()


if PREQUALIFY == 'y':
    if PRINCIPAL <= 199999:                                         # 1-A
        if 1 >= LOAN_TIME <= 15:                                      # 1
            INTR_RATE = 3.63

        elif 16 >= LOAN_TIME <= 20:
            INTR_RATE = 4.04

        elif 21 >= LOAN_TIME <= 30:
            INTR_RATE = 5.77                                           # 1

    elif 2000000 <= PRINCIPAL <= 999999:
        if 1 >= LOAN_TIME <= 15:                                  # 2
            INTR_RATE = 3.02

        elif 16 >= LOAN_TIME <= 20:
            INTR_RATE = 3.27

        elif 21 >= LOAN_TIME <= 30:
            INTR_RATE = 4.66                                       # 2

    if PRINCIPAL >= 1000000:
        if 1 >= LOAN_TIME <= 15:                                  # 3
            INTR_RATE = 2.05

        elif 16 >= LOAN_TIME <= 20:
            INTR_RATE = 2.62
if PREQUALIFY == 'n':                                                  # 2B
    if PRINCIPAL <= 199999:                                         # B1
        if 1 >= LOAN_TIME <= 15:
            INTR_RATE = 4.65

        elif 16 >= LOAN_TIME <= 20:
            INTR_RATE = 4.98

        elif 21 >= LOAN_TIME <= 30:
            INTR_RATE = 6.39

    elif 2000000 <= PRINCIPAL <= 999999:                          # B2
        if 1 >= LOAN_TIME <= 15:
            INTR_RATE = 3.98

        elif 16 >= LOAN_TIME <= 20:
            INTR_RATE = 4.08                                        # 2B

else:
    DECIM_RATE = decimal.Decimal(INTR_RATE)/100
    TOTAL = (round(PRINCIPAL * (1 + (DECIM_RATE / 12)) ** (12 * LOAN_TIME)))

print 'Loan Report for : {}'.format(NAME).upper()
print 'LOAN DURATION   : {}'.format(LOAN_TIME), ' yrs'
print 'PRINCIPAL AMOUNT: {:,}'.format(PRINCIPAL)
print 'PREQUALIFY (Y?N): {}'.format(PREQUALIFY).upper()
print '\nTOTAL          : {}'.format(TOTAL)
