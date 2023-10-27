# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:30:32 2023
Filename: preprint_format_list.py
Purpose: To format the data into list before printout to console
Version: 1.0
@author: No Name
Function List:
(1) add_data()
(2) display_data()
(3) toString()
"""
#*****************************************************************

class DataList:
    def __init__(self):
        self.data_list = []

    def add_data(self, new_data):
        self.data_list.append(new_data)

    def display_data(self):
        print("Data List:")
        for data in self.data_list:
            print(data)

    def toString(self):        
        pass

# Creating an instance of the class
my_data_list = DataList()

# Adding data to the list
my_data_list.add_data("Data 1")
my_data_list.add_data("Data 2")
my_data_list.add_data("Data 3")

# Displaying the data
my_data_list.display_data()
