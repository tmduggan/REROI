#!/usr/bin/python
import numpy as np
import settings as st

pv          =   st.HOUSE_PRICE
nper        =   st.LOAN_TERM
trate       =   st.TAX_RATE


# Interest rate of 4.5%
rate = 0.045 / 12

fv = 0
running_int_total = 0
running_pri_total = 0
running_tax_total = 0
taxes = []
interest = []
principal = []
new_value = []

for per in range(nper):
    if per !=0 and per % 12 == 0: 
        interest += [running_int_total]
        principal += [running_pri_total]
        taxes += [running_tax_total]
        running_int_total = 0
        running_pri_total = 0
        # account for equity appreciation
        nv = pv * 1.07
        new_value += [nv]
    p = -np.ppmt(rate, per, nper, pv)
    i = -np.ipmt(rate, per, nper, pv)
    #print(principal, interest, principal + interest)
    running_int_total += i
    running_pri_total += p
    running_tax_total += i * trate
