# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:52:16 2023
Filename: read_csv.py
Purpose: Class to hold data from csv
Version: 1.0
@author: Chan Fung Chieh
Function List:
(1) Class: CsvDataObject
Definition
"""
#*****************************************************************

import csv
import utilities as ut

# Define a class to hold the data from the CSV
class DataObject:
    def __init__(self, column1, column2, column3, column4, column5, column6, column7):
        self.column1 = column1
        self.column2 = column2
        self.column3 = column3
        self.column4 = column4
        self.column5 = column5
        self.column6 = column6
        self.column7 = column7

        
# Initialize a list to hold the objects
data_objects = []

class ReadCsvFile():
    def __init__(self):
        self.data_dict = {}
    
    def readfile(self, folder_path):        
       
        #Get full folder path name
        full_folder_path = folder_path + '/' + ut.csv_filename
        
        
        # Open the CSV file and read its contents
        with open(full_folder_path, mode='r') as file:
            #Create a csv reader object
            file_read = csv.reader(file)
            
            #Extract the first row as keys
            keys = next(file_read)
        
            #Create an empty dictionary to store the data
            # data_dict = {key: [] for key in keys}
            
            #Loop through each row in the csv file
            for row in file_read:
                #Create temp list to hold data for first row
                temp_list = []
                
                #Assign each value to corresponding key and add to temp list
                for i, key in enumerate(keys):
                    temp_list.append(row[i])
                
                #Add temp_list to data_dict
                self.data_dict[row[0]] = temp_list
                # print(f"{self.data_dict}")
                # self.data_list.append(temp_list)      
                
            return (self.data_dict)
        
    def toString(self):
        return (self.data_dict)
