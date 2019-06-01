#!/usr/bin/python

import numpy as np
from astropy.table import Table, Column
import ROI_helper as gm
import gui_helper as gh

def print_table_1():
    cin_str     =  fmt_crncy(   gm.get_ci()     )
    coc_str     =  fmt_pcnt(    gm.get_coc()    )
    Cap_str     =  fmt_pcnt(    gm.get_cap()    )

    # d/e table will be one time calculations
    x   =  ["Cash in"]
    x   +=  ["Cash on cash"]
    x   +=  ["Cap Rate"]

    y   =  [cin_str]
    y   +=  [coc_str]
    y   +=  [Cap_str]

    u = Table([x, y], names=(' ', 'Total'))

    print( u )

def print_table_2():
    t           =   Table()
    a           =   ["Cash Flow"]
    a           +=  ["Tax Deduction"]
    a           +=  ["Equity Accrued"]
    a           +=  ["NOI"]
    t['Annual'] =   a

    i = 0
    
    nums = [1, 5, 15, 25]
    for i in range(len(nums)):
        str_temp = str(nums[i])
        cf_str      =   fmt_crncy( gm.get_cflow(nums[i])    )
        td_str      =   fmt_crncy(   gm.get_taxd(i)         )
        ea_str      =   fmt_crncy(   gm.get_equity(i)       )
        NOI_str     =   fmt_crncy(   gm.get_NOI(nums[i])    )
        
        t[str_temp] = Column([cf_str, td_str, ea_str, NOI_str])
    print(t)

def fmt_pcnt(x):
    return "{:,.1f}".format( x ) + "%"
def fmt_crncy(x):
    return "$" +   "{:,.0f}".format( x )

print_table_1()
print_table_2()