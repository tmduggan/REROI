#!/usr/bin/python
# Tkinter imported for GUI
from Tkinter import *
import numpy as np
# sys and astropy added for Tables
import sys
from astropy.table import Table

# GLOBAL
TAX_RATE = .22

# ASSUMPTIONS 
# Home owner's insurance = 0.3% based on my last purchase
# Property Tax = 1.69%
# Assuming 300k purchase price
pv = 300000
prop_tax = 0.0169 * pv

# Rent = $2500/month
rent = 2500

# Loan term is 30 years, 12 payments per year
nper = 30 * 12

# Depreciation is over 27.5 years
depr = int(pv / 27.5 )

# Interest rate of 4.5%
rate = 0.045 / 12

fv = 0
running_int_total = 0
running_pri_total = 0
interest = []
principal = []
for per in range(nper):
    if per !=0 and per % 12 == 0: 
        interest += [running_int_total]
        principal += [running_pri_total]
        running_int_total = 0
        running_pri_total = 0
    p = -np.ppmt(rate, per, nper, pv)
    i = -np.ipmt(rate, per, nper, pv)
    #print(principal, interest, principal + interest)
    running_int_total += i
    running_pri_total += p
j = int(raw_input("For what year do you want to know the interest and principal?\n"))

# rent increases at 4% per year
rent = ( rent * (1.04)**j )

# 10% CapEx, 10% Vacancy, 10% Management
expenses = rent * .3
rent = rent - expenses

mortgage = principal[j] + interest[j]


a = ["Total Payment"] 
a += ["Principal"]
a += ["Interest"]
a += ["Taxes"]
a += ["Cash Flow"]
a += ["Tax Deduction"]
a += ["Equity Accrued"]
a += ["Expenses"]

total = principal[j] + interest[j] + prop_tax
cash_flow = rent*12 - mortgage - prop_tax
tax_ded = ( depr + interest[j] ) * TAX_RATE

k = 0
for per in range(j):
    k += principal[per] 
equity_accrued = k / pv
new_value = pv * (1.07)**j
equity_accrued = equity_accrued * new_value

b = ["{:,.2f}".format (total)]
b += ["{:,.2f}".format (principal[j])]
b += ["{:,.2f}".format (interest[j])]
b += ["{:,.2f}".format (prop_tax)]
b += ["{:,.2f}".format (cash_flow)]
b += ["{:,.2f}".format (tax_ded)]
b += ["{:,.2f}".format (equity_accrued)]
b += ["{:,.2f}".format (expenses)]

t = Table([a, b], names=('Annual', j))
print(t)

# I want to know the sum of equity acquired, tax reduction, and cash flow