#!/usr/bin/python

import numpy as np
import decimal

TAX_RATE = .22

# ASSUMPTIONS 
# pv = int(raw_input("What is the purchase price?\n"))
# Assuming 300k purchase price
pv = 300000

# Rent = $2500/month
rent = 2500

# Loan term is 30 years, 12 payments per year
nper = 30 * 12

# Depreciation is over 27.5 years
depr = int(pv / 27.5 )

fv = 0
rate = 0.045 / 12


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
j = int(raw_input("What year do you want to know the interest and principal?\n"))

print("Your total interest in year " + str(j) + \
    " will be $ {:,.2f}".format ( interest[j]  ))
print("Your total principal in year " + str(j) + \
    " will be $ {:,.2f}".format ( principal[j]  ))

# print("Your total depreciation for 27 years (and half for the 28th year) " + \
#     "will be $ {:.2f}".format ( depr  ))

print("Your total tax deduction in year " + str(j) + \
    " will be $ {:,.2f}".format ( ( depr + interest[j] ) * TAX_RATE  ))

rent = rent * (1.04)**j
mortgage = principal[j] + interest[j]

print("Your cash flow in year " + str(j) + \
    " will be $ {:,.2f}".format ( (rent*12 - mortgage) ) \
    + " with monthly rent at ${:,.2f}".format (rent ) + ".")
