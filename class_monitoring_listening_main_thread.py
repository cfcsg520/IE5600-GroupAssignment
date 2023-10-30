# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 23:15:37 2023
Filename: class_monitoring_listening_thread.py
Purpose: Monitor for any new files transferred to "incoming folder". If yes, update the processing queue.
Version: 1.0
@author: No Name
Function List:
(1) class: MonitorFolder()
(2) class: ListeningThread()
(3) def: get_data()
(4) def: get_user_input()
"""
#***

import os
import threading
import time
from queue import Queue
from multiqueue import MultiQueueSystem
import logging

#=================================================================          
#Start of Variables Initialisation
#=================================================================

#Print welcome message
welcome_message = "\nWelcome to QC & Monitoring of Surgical Mask Production"

#Configure logging to text file
logging.basicConfig(filename='message.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#=================================================================
#End of Variables Initialisation
#=================================================================


class MonitorFolderThread(threading.Thread):
    def __init__(self, folder_path, update_queue, stop_event):
        super(MonitorFolderThread, self).__init__()
        self.folder_path = folder_path
        # self.files = set(os.listdir(folder_path))
        self.update_queue = update_queue
        self.stop_event = stop_event
        self.file_set = set()

    def run(self):
        while not self.stop_event.is_set():
            current_files = set(os.listdir(self.folder_path))
            new_files = current_files - self.file_set
            if new_files:
                for file in new_files:
                    self.update_queue.put(file)
                self.file_set.update(new_files)
            time.sleep(5) # Check every 5 seconds

class ListenerThread(threading.Thread):
    def __init__(self, update_queue, data_handler, stop_event):
        super(ListenerThread, self).__init__()
        self.update_queue = update_queue
        self.data_handler = data_handler
        self.stop_event = stop_event

    def run(self):
        add_queue.create_queue("Incoming")
        print(add_queue.toString())
            
        while not self.stop_event.is_set():
            if not self.update_queue.empty():
                update_files = self.update_queue.get()
                self.data_handler(update_files)
                add_queue.enqueue("Incoming", update_files)
                # print("\nDEBUG: [LISTENER] {}".format(add_queue.toString()))
                logging.debug(f"\nDEBUG: [LISTENER] {add_queue.toString()}")
            time.sleep(1)

#Create enqueue to track the files in "Incoming" folder
add_queue = MultiQueueSystem()
        
def get_data(update_files):
        
    if update_files:
        data = update_files     
        # print(f"\nData received from listening thread: {update_files}") 
        logging.debug(f"\nData received from listening thread: {update_files}")     
        return data
    else:
        return None