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

j = int(raw_input("For what year do you want to know the" \
    + " interest and principal?\n"))

k = 0
for per in range(j):
    k += principal[per] 

###############
## Equations ## 
###############
# rent increases at 4% per year
net_rent            =   ( rent * (1.04)**j )
net_taxes           =   taxes[j]
effective_rent      =   net_rent * .9
# NOI is effective rent minus repairs (10%), 
# prop tax (5000), and insurance (1000) 
insurance           =   new_value [j] * .01
NOI                 =   effective_rent - (net_rent*.1) - insurance - 5000
mortgage            =   principal[j] + interest[j]
cash_flow           =   NOI - mortgage - prop_tax
tax_ded             =   ( depr + interest[j] ) * trate
new_value           =   pv * (1.07)**j
equity_accrued      =   new_value * k / pv 
cash_in             =   settings.REHAB + settings.DOWN_PAYMENT + insurance
ROI                 =   100 * NOI / cash_in
cash_on_cash        =   100 * NOI / cash_in
cap_rate            =   100 * NOI / pv
