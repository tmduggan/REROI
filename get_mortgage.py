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
taxes               = []
interest            = []
principal           = []
new_value           = []
net_rent            = []
effective_rent      = []
prop_tax            = []
insurance           = []
NOI                 = []

for per in range(nper):
    

    if per !=0 and per % 12 == 0: 
        nv                      =   pv * 1.07
        ins_temp                =   nv * .01
        net_rent_temp           =   st.RENT * (1.04)**(per/12)
        eff_rent_temp           =   net_rent_temp * .9
        prop_temp               =   st.PROP_TAX_RATE * nv
        NOI_temp                =   eff_rent_temp - (net_rent_temp*.1) - ins_temp - prop_temp

        # print("Eff_rent_temp is " + str(eff_rent_temp) + " for year " + str(per))

        net_rent                +=  [net_rent_temp]
        effective_rent          +=  [eff_rent_temp]
        NOI                     +=  [NOI_temp]
        new_value               +=  [nv]
        insurance               +=  [ins_temp]
        prop_tax                +=  [prop_temp]

        interest            +=  [running_int_total]
        principal           +=  [running_pri_total]
        taxes               +=  [running_tax_total]
        running_int_total   =   0
        running_pri_total   =   0
        
    p                   =   -np.ppmt(rate, per, nper, pv)
    i                   =   -np.ipmt(rate, per, nper, pv)
    running_int_total   +=  i
    running_pri_total   +=  p
    running_tax_total   +=  i * trate


# NOI                 =   effective_rent - (net_rent*.1) - insurance - prop_tax
# mortgage            =   principal[j] + interest[j]
# cash_flow           =   NOI - mortgage - prop_tax
# tax_ded             =   ( st.DEPR + interest[j] ) * trate
# new_value           =   pv * (1.07)**j
# equity_accrued      =   new_value * k / pv 
# cash_in             =   st.REHAB + st.DOWN_PAYMENT + insurance
# ROI                 =   100 * NOI / cash_in
# cash_on_cash        =   100 * NOI / cash_in
# cap_rate            =   100 * NOI / pv