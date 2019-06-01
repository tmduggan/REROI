#!/usr/bin/python
import numpy as np
import settings as st

pv          =   st.HOUSE_PRICE
nper        =   st.LOAN_TERM
rate        =   st.LOAN_INTEREST_RATE

def get_equity(n):
    k = 0
    equity_accrued      = []
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            nv              =   pv * (1.07)**(per/12)
            equity_accrued  +=  [nv * k / pv]
        
        p                   =   -np.ppmt(rate, per, nper, pv)
        k                   +=  p
    return equity_accrued[n]

def get_taxd(n):
    running_int_total   = 0
    tax_ded             = []    #
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            taxd_temp               =   ( st.DEPR + running_int_total ) * st.TAX_RATE
            tax_ded                 +=  [taxd_temp]
            running_int_total       =   0
        ##
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i
    return tax_ded[n]

def get_NOI(n):
    NOI                 = []    #
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            # new value of house
            nv                      =   pv * (1.07)**(per/12)
            # property insurance 1%
            ins_rate                =   .0042
            ins_temp                =   nv * ins_rate
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
    return NOI[n]

def get_cflow(n):
    cash_flow           = []
    running_pri_total   = 0
    running_int_total   = 0
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            # total mortgage
            mrg_temp                =   running_int_total + running_pri_total
            iter_i                  =   per/12 - 1
            NOI_temp                =   get_NOI( iter_i )
            cash_flow               +=  [NOI_temp - mrg_temp]

            # reset intermediate values
            running_int_total       =   0
            running_pri_total       =   0
        p                   =   -np.ppmt(rate, per, nper, pv)
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i
        running_pri_total   +=  p
    return cash_flow[n]

def get_ci():
    return st.REHAB + st.DOWN_PAYMENT + (st.HOUSE_PRICE_FULL * .01)

def get_coc():
    return 100 * get_NOI(1) / get_ci()

def get_cap():
    return 100 * get_NOI(1) / st.HOUSE_PRICE

#############################
#       Unused Modules      #
#############################
def get_ROI():
    return 100 * get_NOI(1) / get_ci()

def get_p(n):
    fv = 0
    running_pri_total   = 0
    principal           = []

    for per in range(nper):
        

        if per !=0 and per % 12 == 0: 
            principal               +=  [running_pri_total]
            running_pri_total       =   0
            
        p                   =   -np.ppmt(rate, per, nper, pv)
        running_pri_total   +=  p
    return principal(n)

def get_i(n):
    fv = 0
    running_int_total   = 0
    interest            = []

    for per in range(nper):
        

        if per !=0 and per % 12 == 0: 
            interest                +=  [running_int_total]
            running_int_total       =   0
            
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i
    return interst[n]

def get_t(n):
    fv = 0
    running_int_total   = 0
    running_tax_total   = 0

    taxes               = []

    for per in range(nper):

        if per !=0 and per % 12 == 0: 
            taxes                   +=  [running_tax_total]
            running_int_total       =   0
        i                   =   -np.ipmt(rate, per, nper, pv)
        running_int_total   +=  i
        running_tax_total   +=  i * trate
    return taxes[n]