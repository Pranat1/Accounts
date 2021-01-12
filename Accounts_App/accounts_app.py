#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Dec 28 19:14:10 2020

@author: pranatagrawal
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Thu Aug  6 01:38:20 2020

@author: pranatagrawal
"""



import tkinter as tk
from tkinter import ttk
from Accounts_App import Account, HelloWorld
from pyexcel_ods import get_data
import os

path = os.getcwd()

def main():
    list_of_accounts = []
    wb = get_data(path + "/All_accounts.ods")
    account_files = wb["Sheet1"]
    account_files = account_files[1:]
    for i in range(len(account_files)-1):
        if account_files[i] != []:
            wb1 = get_data(path + account_files[i][1])
            wb1_keys = list(wb1.keys())
            for j in range(len(wb1_keys)):
                account_data = wb1[wb1_keys[j]]
                list_of_accounts.append(Account(account_data, account_files[i][1], wb1_keys[j], account_files[i][1]))
    return list_of_accounts

list_data = main()

class Accounts_App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all_accounts = list_data
        self.p = 1
        self.container = ttk.Frame(self)
        self.container.grid()
        self.container.columnconfigure(0, weight=1)
        self.discription_frame = 1
        self.frames = {}
        hello_world_frame = HelloWorld(self.all_accounts, self.container, self, list_data)
        hello_world_frame.grid(row=0, column=0, sticky="NESW")
        self.frames[HelloWorld] = hello_world_frame
        self.show_frame(HelloWorld)



    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()



app = Accounts_App()
app.mainloop()
