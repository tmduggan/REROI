#!/usr/bin/python

import numpy as np
from astropy.table import Table
import logic as l

brk_line    =   "-------"
cf_str      =   "$" +   "{:,.2f}".format(l.cash_flow)
td_str      =   "$" +   "{:,.2f}".format(l.tax_ded)
ea_str      =   "$" +   "{:,.2f}".format(l.equity_accrued)
NOI_str     =   "$" +   "{:,.2f}".format(l.NOI)
cin_str     =   "$" +   "{:,.2f}".format(l.cash_in)
coc_str     =           "{:,.2f}".format(l.cash_on_cash)    + "%"
Cap_str     =           "{:,.2f}".format(l.cap_rate)        + "%"
ROI_str     =           "{:,.2f}".format(l.ROI)             + "%"

a   =   ["Cash Flow"]
a   +=  ["Tax Deduction"]
a   +=  ["Equity Accrued"]
a   +=  ["NOI"]
a   +=  ["Cash in"]
a   +=  [brk_line]
a   +=  ["Cash on cash"]
a   +=  ["Cap Rate"]
a   +=  ["ROI"]

b   =   [cf_str]
b   +=  [td_str]
b   +=  [ea_str]
b   +=  [NOI_str]
b   +=  [cin_str]
b   +=  [brk_line]
b   +=  [coc_str]
b   +=  [Cap_str]
b   +=  [ROI_str]

t = Table([a, b], names=('Annual', l.j))
print(t)