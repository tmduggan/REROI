#!/usr/bin/python
import settings as st
import numpy as np
import get_mortgage as gm

pv      =   st.HOUSE_PRICE


j = st.j

equity_accrued      =   gm.new_value[j]

###############
## Equations ## 
###############
insurance           =   gm.insurance[j]         
NOI                 =   gm.NOI[j]               #
cash_flow           =   gm.cash_flow[j]         #
tax_ded             =   gm.tax_ded[j]

# tax_ded             =   ( st.DEPR + interest[j] ) * trate


cash_in             =   st.REHAB + st.DOWN_PAYMENT + insurance
ROI                 =   100 * NOI / cash_in
cash_on_cash        =   100 * NOI / cash_in
cap_rate            =   100 * NOI / pv

# I want an array of 
# # Tax deduction per year
# # equity accrued per year
# # NOI per year