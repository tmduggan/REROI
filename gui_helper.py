#!/usr/bin/python
# import Tkinter
from Tkinter import *
import settings as st
import numpy as np

master = Tk() 
master.title('Property Analysis') 


Label(master, text='Purchase Price').grid(row=0) 
Label(master, text='Down Payment').grid(row=1) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

button = Button(master, text='Stop', command=master.destroy) 
button.grid(row=2, column=1)

def submit_values():
    s1 = float(e1.get())
    s2 = e2.get()
    rate        =   st.LOAN_INTEREST_RATE
    nper        =   st.LOAN_TERM
    k = 0
    equity_accrued      = []
    for per in range (nper):
        if per !=0 and per % 12 == 0:
            nv              =   s1 * (1.07)**(per/12)
            equity_accrued  +=  [nv * k / s1]
        
        p                   =   -np.ppmt(rate, per, nper, s1)
        k                   +=  p
    print("equity accrued in year 1 is " +  str(equity_accrued[1]) )


button = Button(master, text='Submit', command=submit_values) 
button.grid(row=3, column=1)




mainloop() 
