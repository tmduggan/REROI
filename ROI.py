#!/usr/bin/python


import numpy as np
from astropy.table import Table
import settings
import logic

cash_flow = logic.cash_flow
tax_ded = logic.tax_ded
equity_accrued = logic.equity_accrued

a =  ["Cash Flow"]
a += ["Tax Deduction"]
a += ["Equity Accrued"]


b = ["{:,.2f}".format (cash_flow)]
b += ["{:,.2f}".format (tax_ded)]
b += ["{:,.2f}".format (equity_accrued)]


t = Table([a, b], names=('Annual', logic.j))
print(t)

# I want to know how much return I am getting, not counting 
# mortgage. I want to know my ROI which should be equal to
# (Rent Income + Equity accrued + tax deduction) 
# - (down payment + prop tax * J)
