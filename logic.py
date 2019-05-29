#!/usr/bin/python
import settings
import numpy as np
import get_mortgage as gm

pv = settings.HOUSE_PRICE
rent = settings.RENT
trate = settings.TAX_RATE

# Depreciation is over 27.5 years
depr = int(pv * .8 / 27.5 )

taxes = gm.taxes
interest = gm.interest
principal = gm.principal
new_value = gm.new_value

j = int(raw_input("For what year do you want to know the" \
    + " interest and principal?\n"))

k = 0
for per in range(j):
    k += principal[per] 

###############
## Equations ## 
###############
net_rent            =   ( rent * (1.04)**j )
net_taxes           =   taxes[j]
effective_rent      =   net_rent * .9
prop_tax            =   settings.PROP_TAX_RATE * new_value[j]
insurance           =   new_value [j] * .01
NOI                 =   effective_rent - (net_rent*.1) - insurance - prop_tax
mortgage            =   principal[j] + interest[j]
cash_flow           =   NOI - mortgage - prop_tax
tax_ded             =   ( depr + interest[j] ) * trate
new_value           =   pv * (1.07)**j
equity_accrued      =   new_value * k / pv 
cash_in             =   settings.REHAB + settings.DOWN_PAYMENT + insurance
ROI                 =   100 * NOI / cash_in
cash_on_cash        =   100 * NOI / cash_in
cap_rate            =   100 * NOI / pv
