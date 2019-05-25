#!/usr/bin/python
import settings
import numpy as np

pv = settings.HOUSE_PRICE
prop_tax = settings.PROP_TAX_RATE * pv
rent = settings.RENT
nper = settings.LOAN_TERM
trate = settings.TAX_RATE

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

total = principal[j] + interest[j] + prop_tax
cash_flow = rent*12 - mortgage - prop_tax
tax_ded = ( depr + interest[j] ) * trate

k = 0
for per in range(j):
    k += principal[per] 
equity_accrued = k / pv
new_value = pv * (1.07)**j
equity_accrued = equity_accrued * new_value