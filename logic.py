#!/usr/bin/python
import settings as st
import numpy as np
import get_mortgage as gm

pv      =   st.HOUSE_PRICE
rent    =   st.RENT
trate   =   st.TAX_RATE

interest = gm.interest
principal = gm.principal
new_value = gm.new_value

j = st.j

k = 0
for per in range(j):
    k += principal[per] 

###############
## Equations ## 
###############
net_rent            =   gm.net_rent[j]
net_taxes           =   gm.taxes[j]
effective_rent      =   gm.effective_rent[j]
prop_tax            =   gm.prop_tax[j]
insurance           =   gm.insurance[j]
NOI                 =   effective_rent - (net_rent*.1) - insurance - prop_tax
# NOI                 =   gm.NOI[j]
mortgage            =   principal[j] + interest[j]
cash_flow           =   NOI - mortgage - prop_tax
tax_ded             =   ( st.DEPR + interest[j] ) * trate
new_value           =   pv * (1.07)**j
equity_accrued      =   new_value * k / pv 
cash_in             =   st.REHAB + st.DOWN_PAYMENT + insurance
ROI                 =   100 * NOI / cash_in
cash_on_cash        =   100 * NOI / cash_in
cap_rate            =   100 * NOI / pv

# I want an array of 
# # cash flow per year
# # Tax deduction per year
# # equity accrued per year
# # NOI per year