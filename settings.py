#!/usr/bin/python

# I want to know how good/bad of an investment
# buying different properties are.

# # GLOBAL
TAX_RATE = .22
# HOUSE_PRICE_FULL not currently used
# HOUSE_PRICE_FULL = int(raw_input("How much is the house?\n"))
HOUSE_PRICE_FULL = 300000
# DOWN_PAYMENT not currently used
# DOWN_PAYMENT = int(raw_input("What is the down payment?\n"))
DOWN_PAYMENT = 10000
# REHAB = int(raw_input("What is the rehab cost?\n"))
REHAB = 20000

HOUSE_PRICE = HOUSE_PRICE_FULL - DOWN_PAYMENT
PROP_TAX_RATE = 0.0169
# Rent = $2500/month
RENT = 2500 * 12
# Loan term is 30 years, 12 payments per year
LOAN_TERM = 30 * 12

# Depreciation is over 27.5 years
DEPR = int(HOUSE_PRICE_FULL * .8 / 27.5 )
