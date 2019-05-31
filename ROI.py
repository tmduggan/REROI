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
    str_temp = str(nums[i])
    cf_str      =   "$" +   "{:,.0f}".format(   gm.get_cflow(nums[i])   )
    td_str      =   "$" +   "{:,.0f}".format(   gm.get_taxd(i)          )
    ea_str      =   "$" +   "{:,.0f}".format(   gm.get_equity(i)        )
    NOI_str     =   "$" +   "{:,.0f}".format(   gm.get_NOI(nums[i])     )
    
    t[str_temp] = Column([cf_str, td_str, ea_str, NOI_str])


cin_str     =   "$" +   "{:,.2f}".format(   gm.get_ci()     )
coc_str     =           "{:,.2f}".format(   gm.get_coc()    ) + "%"
Cap_str     =           "{:,.2f}".format(   gm.get_cap()    ) + "%"

# d/e table will be one time calculations
x   =  ["Cash in"]
x   +=  ["Cash on cash"]
x   +=  ["Cap Rate"]

y   =  [cin_str]
y   +=  [coc_str]
y   +=  [Cap_str]

u = Table([x, y], names=(' ', 'Total'))
print('\n')
print(u)
print('\n')
print(t)
