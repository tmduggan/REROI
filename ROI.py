#!/usr/bin/python

import numpy as np
from astropy.table import Table
from astropy.table import Column
import get_mortgage as gm


a   =   ["Cash Flow"]
a   +=  ["Tax Deduction"]
a   +=  ["Equity Accrued"]
a   +=  ["NOI"]

cf_str      =   "$" +   "{:,.2f}".format(   gm.cash_flow[1]         )
td_str      =   "$" +   "{:,.2f}".format(   gm.tax_ded[1]           )
ea_str      =   "$" +   "{:,.2f}".format(   gm.equity_accrued[1]    )
NOI_str     =   "$" +   "{:,.2f}".format(   gm.NOI[1]               )

b   =   [cf_str]
b   +=  [td_str]
b   +=  [ea_str]
b   +=  [NOI_str]

cf_str      =   "$" +   "{:,.2f}".format(   gm.cash_flow[5]         )
td_str      =   "$" +   "{:,.2f}".format(   gm.tax_ded[5]           )
ea_str      =   "$" +   "{:,.2f}".format(   gm.equity_accrued[5]    )
NOI_str     =   "$" +   "{:,.2f}".format(   gm.NOI[5]               )

c   =   [cf_str]
c   +=  [td_str]
c   +=  [ea_str]
c   +=  [NOI_str]

cf_str      =   "$" +   "{:,.2f}".format(   gm.cash_flow[15]         )
td_str      =   "$" +   "{:,.2f}".format(   gm.tax_ded[15]           )
ea_str      =   "$" +   "{:,.2f}".format(   gm.equity_accrued[15]    )
NOI_str     =   "$" +   "{:,.2f}".format(   gm.NOI[15]               )

d   =   [cf_str]
d   +=  [td_str]
d   +=  [ea_str]
d   +=  [NOI_str]


cin_str     =   "$" +   "{:,.2f}".format(   gm.cash_in      )
coc_str     =           "{:,.2f}".format(   gm.cash_on_cash  )    + "%"
Cap_str     =           "{:,.2f}".format(   gm.cap_rate      )        + "%"
ROI_str     =           "{:,.2f}".format(   gm.ROI           )             + "%"

# d/e table will be one time calculations
x   =  ["Cash in"]
x   +=  ["Cash on cash"]
x   +=  ["Cap Rate"]
x   +=  ["ROI"]

y   =  [cin_str]
y   +=  [coc_str]
y   +=  [Cap_str]
y   +=  [ROI_str]




# b   =   [cf_str]
# b   +=  [td_str]
# b   +=  [ea_str]
# b   +=  [NOI_str]


t = Table([a, b, c, d], names=('Annual', '1', '5', '15'))
u = Table([x, y], names=('One Time Calcuations', 'Total'))
print('\n')
print(u)
print('\n')
print(t)


# Now I want a table to show the numbers at year 1, 5, 10, and 20
# 