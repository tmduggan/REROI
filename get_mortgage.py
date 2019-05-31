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
NOI                 = []    #
cash_flow           = []    #
tax_ded             = []    #
equity_accrued      = []




class get_equity:
    k = 0
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            nv              =   pv * (1.07)**(per/12)
            equity_accrued  +=  [nv * k / pv]
        
        p                   =   -np.ppmt(rate, per, nper, pv)
        k                   +=  p

class get_taxd:
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            taxd_temp               =   ( st.DEPR + running_int_total ) * trate
            tax_ded                 +=  [taxd_temp]
            running_int_total       =   0
        ##
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i

class get_NOI:
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            # new value of house
            nv                      =   pv * (1.07)**(per/12)
            # property insurance 1%
            ins_temp                =   nv * .01
            # property tax 1.69%
            prop_temp               =   st.PROP_TAX_RATE * nv
            # rent with appropriate annual increase
            net_rent_temp           =   st.RENT * (1.04)**(per/12)
            # effective rent after deducting 10% for repairs
            eff_rent_temp           =   net_rent_temp * .9

            # intermediate values with 10% off rent for management
            ert                     =   eff_rent_temp - (net_rent_temp*.1)
            ipr                     =   ins_temp + prop_temp
        
            NOI                     +=  [ert - ipr]

class get_cflow:
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            # total mortgage
            mrg_temp                =   running_int_total + running_pri_total
            iter_i                  =   per/12 - 1
            NOI_temp                =   NOI[ iter_i ]
            cash_flow               +=  [NOI_temp - mrg_temp]

            # reset intermediate values
            running_int_total       =   0
            running_pri_total       =   0
        p                   =   -np.ppmt(rate, per, nper, pv)
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i
        running_pri_total   +=  p

cash_in             =   st.REHAB + st.DOWN_PAYMENT + (st.HOUSE_PRICE_FULL * .01)
ROI                 =   100 * NOI[1] / cash_in
cash_on_cash        =   100 * NOI[1] / cash_in
cap_rate            =   100 * NOI[1] / st.HOUSE_PRICE