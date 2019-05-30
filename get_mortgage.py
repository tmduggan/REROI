#!/usr/bin/python
import numpy as np
import settings as st

pv          =   st.HOUSE_PRICE
nper        =   st.LOAN_TERM
trate       =   st.TAX_RATE


# Interest rate of 4.5%
rate = 0.045 / 12

fv = 0
running_int_total   = 0
running_pri_total   = 0
running_tax_total   = 0
new_value           = []
insurance           = []
NOI                 = []    #
mortgage            = []
cash_flow           = []    #
tax_ded             = []    #
equity_accrued      = []

k = 0

for per in range(nper):
    

    if per !=0 and per % 12 == 0: 
        nv                      =   pv * (1.07)**(per/12)
        ins_temp                =   nv * .01
        net_rent_temp           =   st.RENT * (1.04)**(per/12)
        eff_rent_temp           =   net_rent_temp * .9
        prop_temp               =   st.PROP_TAX_RATE * nv
        mrg_temp                =   running_int_total + running_pri_total
        ert                     =   eff_rent_temp - (net_rent_temp*.1)
        ipr                     =   ins_temp + prop_temp
        

        NOI_temp                =   ert - ipr
        cflow_temp              =   NOI_temp - mrg_temp - prop_temp
        taxd_temp               =   ( st.DEPR + running_int_total ) * trate

        equity_accrued          +=  nv * k / pv         
        tax_ded                 +=  [taxd_temp]
        NOI                     +=  [NOI_temp]
        new_value               +=  [nv]
        insurance               +=  [ins_temp]
        cash_flow               +=  [cflow_temp]

        # interest                +=  [running_int_total]
        # principal               +=  [running_pri_total]
        # taxes                   +=  [running_tax_total]
        running_int_total       =   0
        running_pri_total       =   0
        
    p                   =   -np.ppmt(rate, per, nper, pv)
    i                   =   -np.ipmt(rate, per, nper, pv)
    running_int_total   +=  i
    running_pri_total   +=  p
    k                   +=  p
    running_tax_total   +=  i * trate

# new_value           =   pv * (1.07)**j
# equity_accrued      =   new_value * k / pv 
# cash_in             =   st.REHAB + st.DOWN_PAYMENT + insurance
# ROI                 =   100 * NOI / cash_in
# cash_on_cash        =   100 * NOI / cash_in
# cap_rate            =   100 * NOI / pv