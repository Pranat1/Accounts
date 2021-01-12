#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:44:52 2020

@author: pranatagrawal
"""

path =  "/Users/pranatagrawal/Desktop/Lucknow_Marbles/Accounts_App/"

import tkinter as tk
from tkinter import ttk
from pyexcel_ods import get_data, save_data
import os

class Account:
    def __init__(self, account_data, file_directory, name_of_account, file_name):

        #:param color:
        #:param price:
        #:param stock: is a dictionary with keys as length, width and seriel number.
        #:param size:
        #:param quality:
        self.file_directory = file_directory
        self.name_of_account = name_of_account
        self.total_min = 0.0
        self.total_plus = 0.0
        self.entries = {}
        self.account_data = account_data
        self.file_name = file_name
        account_data = account_data[1:]
        print(account_data)
        for i in range(len(account_data)-1):
            if account_data[i] != []:
                if len(account_data[i]) == 3:
                    if account_data[i][1] != "" and account_data[i][2] != "":
                        self.total_plus += account_data[i][1]
                        self.total_min += account_data[i][2]
            


class HelloWorld(ttk.Frame):

    def __init__(self, all_accounts, parent, self_, list_data):
        super().__init__(parent)
        self.all_accounts = all_accounts
        self.list_of_entries = []
        self.myentries = []
        self.labels_discription = []
        self.corrent_stone = []
        self.my_buttons_cut =[]
        self.labels_discription_cut = []
        list_of_accounts_ = []
        clicked = tk.StringVar()
        clicked_1 = tk.StringVar()
        for i in range(len(self.all_accounts)):
            list_of_accounts_.append(self.all_accounts[i].name_of_account)
        drop = ttk.OptionMenu(self, clicked, *list_of_accounts_)
        drop_1 = ttk.OptionMenu(self, clicked_1, *list_of_accounts_)
        drop.grid(row=0, column=0)
        drop_1.grid(row=0, column=1)
        plus_minus_entry = ttk.Entry(self)
        plus_minus_entry.grid(row = 1, column= 1)
        entry_date = ttk.Entry(self)
        entry_date.grid(row = 1, column = 2)
        options = {}
        for i in range(len(self.all_accounts)):
            options[self.all_accounts[i].name_of_account] = i
        submit_button = ttk.Button(self, text = "Submit", command = lambda: self.update(self.all_accounts[options[clicked.get()]], self.all_accounts[options[clicked_1.get()]], plus_minus_entry.get(), entry_date.get()))
        submit_button.grid(row = 1, column= 0)
        
        
        
    def update(self, file_1, file_2, amount, date):
        file1 = get_data(path + file_1.file_name)
        file2 = get_data(path + file_2.file_name)
        data_1 = file1[file_1.name_of_account]
        data_2 = file2[file_2.name_of_account]
        del file1[file_1.name_of_account]
        del file2[file_2.name_of_account]
        data_1.append([date, amount, 0])
        data_2.append([date, 0, amount])
        file1.update({file_1.name_of_account: data_1})
        file2.update({file_2.name_of_account: data_2})
        os.remove(path + file_1.file_name)
        save_data(path + file_1.file_name,  file1)
        os.remove(path + file_2.file_name)
        save_data(path + file_2.file_name,  file2)
        
        
        
        
        