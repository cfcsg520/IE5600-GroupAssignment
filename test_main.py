# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:09:30 2023
Filename: test_main.py
Purpose: Entry execution point for QC & Monitoring of Surgical Mask Production
Version: 1.0
@author: Chan Fung Chieh
Function List:
(1) main - main entry point for "QC & Monitoring of Surgical Mask Production Program"
Definition
"""
#*****************************************************************

#=================================================================
#Start of Import function
#=================================================================
#Import from external Python files
import class_monitoring_listening_main_thread as mt
import os
from queue import Queue
import threading
import time
from multiqueue import MultiQueueSystem
import shutil
from read_csv import ReadCsvFile
import utilities as ut
from query_batch_information import QueryBatchInformation

#=================================================================
#End of Import
#=================================================================

#*****************************************************************
#=================================================================
#Start of Local Function Declarations
#=================================================================
def user_choice_input(input_queue):

    # while True:
    user_input = input("Enter your choice: ").upper()
    input_queue.put(user_input)

#=================================================================
#End of Local Functions Declarations
#=================================================================
#=================================================================          
#Start of Variables Initialisation
#=================================================================

#Print welcome message
welcome_message = "\nWelcome to QC & Monitoring of Surgical Mask Production"

# #Configure logging to text file
# logging.basicConfig(filename='message.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#=================================================================
#End of Variables Initialisation
#=================================================================
#=================================================================
#Start of Main Code
#=================================================================
def main():
    
    #Create queue for communicating user_input
    input_queue = Queue()
    
    while True:
   
        #Print welcome message
        for i in range (0, len(welcome_message)):
            print("*", end="")
            i +=1
        
        print(f"{welcome_message}")
    
        for i in range (0, len(welcome_message)):
            if (i == len(welcome_message) - 1):
                print("*")
            else:
                print("*", end="")
            i +=1
        
        #Print rest of options
        print("1.  Start Service")
        print("2.  Display Queue")
        print("3.  Load Dataset")
        print("4.  Query Batch Result")
        print("5.  Query Range of Batch(es) Result")        
        print("X. Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "1": #Start Service                        
            # Provide the path of the folder you want to monitor
            current_folder_path = os.getcwd()
            update_current_folder_path = current_folder_path.replace("\\", "/")
            folder_path = update_current_folder_path + ut.incoming_folder  # Replace with the actual path
            mt.logging.debug(f"DEBUG: [MAIN] Active path: {folder_path}")
            # print(f"Active path: {folder_path}")
            
            # Create a shared queue
            shared_queue = Queue()
            mt.stop_event = threading.Event()

            # Create and start the monitoring thread
            monitor_thread = mt.MonitorFolderThread(folder_path, shared_queue, mt.stop_event)
            monitor_thread.daemon = True
            monitor_thread.start()
            mt.logging.debug("DEBUG: [MAIN] monitor_thread started")
            # print("DEBUG: monitor_thread started")

            # Create and start the listener thread
            listener_thread = mt.ListenerThread(shared_queue, mt.get_data, mt.stop_event)
            listener_thread.daemon = True
            listener_thread.start()
            mt.logging.debug("DEBUG: [MAIN] listener_thread started")
            # print("DEBUG: listener_thread started")
                      
            while not mt.stop_event.is_set():
                data = mt.get_data(0)
                if data:
                    # print(f"DEBUG: [LISTENER] Received update: {data}")
                    mt.logging.debug(f"DEBUG: [LISTENER] Received update: {data}")
                else:
                    # print("DEBUG: [LISTENER] No update")
                    mt.logging.debug("DEBUG: [LISTENER] No update")
                time.sleep(1)
                break          
            
        elif choice == "2": #Display Queue
            print(f"DEBUG: [MAIN] Queues in line: {mt.add_queue.toString()}")
            mt.logging.debug(f"DEBUG: [MAIN] Queues in line: {mt.add_queue.toString()}")
                
        elif choice == "3": #Load Dataset
            print("Load new dataset from queue")
            read_file = ReadCsvFile()

            #Get and Set folder path
            current_folder_path = os.getcwd()
            update_current_folder_path = current_folder_path.replace("\\", "/")
            folder_path = update_current_folder_path + ut.incoming_folder  # Replace with the actual path       

            ut.data_list = read_file.readfile(folder_path)
            print(f"DEBUG: [MAIN] {ut.data_list}")
            if True:
                pass
            # queue_length = queue_size("Incoming") #CFC: Stop here
            # if queue_length != 0:
            #     print (f"Items in queue: {queue_length}")
            
        elif choice == "4": #Query Single Batch Result
            print("DEBUG: [MAIN] Query single batch information")
            user_input = input("Enter batch number in format DDMMYYABCD (e.g. 2309230001): ")
            query_batch = QueryBatchInformation()
            result = query_batch.query_single_batch(user_input)
            print(f"DEBUG: [MAIN] {result}")
            
        elif choice == "5": #Query Range of Batch(es) Results
            print("DEBUG: [MAIN] Query batch information")
            
            while True:
                try:
                    start_range, end_range = input("Enter range of batches, separated by commas (e.g. 2309230001, 2309230009): ").split(',')            
                    
                    #Remove whitespace
                    start_range = start_range.strip()
                    end_range = end_range.strip()
                    print(f"DEBUG: [MAIN] start:{start_range}, end:{end_range}")
                    break
                
                except ValueError:
                    print("DEBUG: [MAIN] Insufficient values. Please re-enter valid range of batch number for query")
            
            query_batch = QueryBatchInformation()
            result = query_batch.query_multiple_batch(start_range, end_range)
            print(f"DEBUG: [MAIN] {result}")

            
        elif choice == "X":
            print("\nGoodbye...\n")           

            # Check if the threads have stopped
            try:
                while True:
                    if not monitor_thread.is_alive() and not listener_thread.is_alive():               
                        print("DEBUG: [MAIN] All threads are stopped successfully")
                        break
                    else:                
                        #Stop threads
                        print("DEUBG: [MAIN] Stopping Threads..")
                        #Stop MonitorFolder and Listener Threads
                        mt.stop_event.set()
                        monitor_thread.join()
                        listener_thread.join()
                        time.sleep(2)
            except UnboundLocalError:
                print("DEBUG: [MAIN] No active threads.")
                break
                
        else:
            print("Invalid choice. Please select a valid option.")

    
if __name__ == '__main__': 
        main()

#=================================================================
#End of Main function
#=================================================================
#=================================================================
#Start of Output function
#=================================================================      
#For Output
#=================================================================
#End of Output function
#=================================================================