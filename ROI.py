#!/usr/bin/python

import numpy as np
from astropy.table import Table, Column
import get_mortgage as gm


t = Table()
a   =   ["Cash Flow"]
a   +=  ["Tax Deduction"]
a   +=  ["Equity Accrued"]
a   +=  ["NOI"]
t['Annual'] = a

i = 0
tot = 4
nums = [1, 5, 15, 25]
for i in range(tot):
    cf_str      =   "$" +   "{:,.0f}".format(   gm.cash_flow[nums[i]]         )
    td_str      =   "$" +   "{:,.0f}".format(   gm.tax_ded[nums[i]]           )
    ea_str      =   "$" +   "{:,.0f}".format(   gm.equity_accrued[nums[i]]    )
    NOI_str     =   "$" +   "{:,.0f}".format(   gm.NOI[nums[i]]               )
    str_temp = str(nums[i])
    t[str_temp] = Column([cf_str, td_str, ea_str, NOI_str])


cin_str     =   "$" +   "{:,.2f}".format(   gm.cash_in      )
coc_str     =           "{:,.2f}".format(   gm.cash_on_cash  )    + "%"
Cap_str     =           "{:,.2f}".format(   gm.cap_rate      )        + "%"
# ROI_str     =           "{:,.2f}".format(   gm.ROI           )             + "%"

# d/e table will be one time calculations
x   =  ["Cash in"]
x   +=  ["Cash on cash"]
x   +=  ["Cap Rate"]
# x   +=  ["ROI"]

y   =  [cin_str]
y   +=  [coc_str]
y   +=  [Cap_str]
# y   +=  [ROI_str]

u = Table([x, y], names=(' ', 'Total'))
print('\n')
print(u)
print('\n')
print(t)
