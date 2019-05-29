#!/usr/bin/python

import numpy as np
from astropy.table import Table
import settings
import logic as l


a   =   ["Cash Flow"]
a   +=  ["Tax Deduction"]
a   +=  ["Equity Accrued"]
a   +=  ["ROI"]
a   +=  ["NOI"]
a   +=  ["Cap Rate"]
a   +=  ["Cash in"]
a   +=  ["Cash on cash"]

cf_str      =   "$" +   "{:,.2f}".format(l.cash_flow)
td_str      =   "$" +   "{:,.2f}".format(l.tax_ded)
ea_str      =   "$" +   "{:,.2f}".format(l.equity_accrued)
ROI_str     =           "{:,.2f}".format(l.ROI)             + "%"
NOI_str     =   "$" +   "{:,.2f}".format(l.NOI)
Cap_str     =           "{:,.2f}".format(l.cap_rate)        + "%"
cin_str     =   "$" +   "{:,.2f}".format(l.cash_in)
coc_str     =           "{:,.2f}".format(l.cash_on_cash)    + "%"

b   =   [cf_str]
b   +=  [td_str]
b   +=  [ea_str]
b   +=  [ROI_str]
b   +=  [NOI_str]
b   +=  [Cap_str]
b   +=  [cin_str]
b   +=  [coc_str]

t = Table([a, b], names=('Annual', l.j))
print(t)

# I want to know how much return I am getting, not counting 
# mortgage. I want to know my ROI which should be equal to
# (Rent Income + Equity accrued + tax deduction) 
# - (down payment + prop tax * J)

# print("Your NOI is $" + NOI_str)
# print("Your ROI is " + ROI_str + "%.")
# print("Your Cap Rate is " + Cap_str + "%.")
# print("Generating $" + NOI_str + " per year on $" + ote_str)
# print("Cash on cash return is " + coc_str + "%")