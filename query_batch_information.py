# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:30:34 2023
Filename: query_batch_information.py
Purpose: Provide methods to query the batch information from dataset
Version: 1.0
@author: Chan Fung Chieh
Function List:
Definition:
"""
#*****************************************************************

import utilities as ut

class UserDefinedQueryMethod():
    
    def __init__(self):
        
        pass
    
    def toString(self): #use this for easy dump out data from the Parent Class
        
        pass

class QueryBatchInformation(UserDefinedQueryMethod):
    def __init__(self):
        
        super().__init__()
        
    
    def query_single_batch(self, batch_nos):
        print(f"{ut.data_list}")
        print(f"{batch_nos}")
        check_valid_batch = len(ut.data_list)
        if check_valid_batch == 0:
            print("[QuerySingleBatch] No valid database")
            print("[QuerySingleBatch] Return option to Load database")
            
            return False
        else:
            for key, value in ut.data_list.items():
                if key == batch_nos:
                    print(f"[QuerySingleBatch] Batch No: {key}, Results: {value}")
                    return key, value                
    
    def query_multiple_batch(self, start_batch_nos, end_batch_nos):
        print(f"DEBUG: [QueryMultipleBatch] database: {ut.data_list}")
        print(f"DEBUG: [QueryMultipleBatch] start:{start_batch_nos}, end:{end_batch_nos}")
        check_valid_batch = len(ut.data_list)
        if check_valid_batch == 0:
            print("[QueryMultipleBatch] No valid database")
            print("[QueryMultipleBatch] Return option to Load database")
            
            return False
        else:
            #create temp_list to hold the query batch(es) data
            temp_list = {}
            key_temp = 0            
            for key, value in ut.data_list.items():
                try:
                    if isinstance (key, str):
                        key_temp = int(key)
                except TypeError:
                    print("DEBUG: [QueryMultipleBatch] Unable to proceed due to incorrect Batch Number type")
                    return False
                    
                if key_temp >= int(start_batch_nos) and key_temp <= int(end_batch_nos):
                    print(f"[QueryMultipleBatch] Batch No: {key}, Results: {value}")
                    temp_list[key] = value
            return temp_list
    
    def toString(self):
        pass
        