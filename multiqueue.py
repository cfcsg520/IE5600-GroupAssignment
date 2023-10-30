# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:14:42 2023

@author: cfc_1
"""

class UserDefinedDataStructure():
    
    def __init__(self):
        
        pass
    
    def toString(self): #use this for easy dump out data from the Parent Class
        
        pass

class MultiQueueSystem(UserDefinedDataStructure):
    def __init__(self):
        
        super().__init__()
        
        self.queues = {}

    def create_queue(self, queue_name):
        if queue_name in self.queues:
            raise ValueError(f"Queue with name {queue_name} already exists.")
        self.queues[queue_name] = []

    def enqueue(self, queue_name, data):
        if queue_name not in self.queues:
            raise ValueError(f"Queue with name {queue_name} does not exist.")
        self.queues[queue_name].append(data)

    def dequeue(self, queue_name):
        if queue_name not in self.queues:
            raise ValueError(f"Queue with name {queue_name} does not exist.")
        if not self.queues[queue_name]:
            raise ValueError(f"Queue with name {queue_name} is empty.")
        return self.queues[queue_name].pop(0)

    def queue_size(self, queue_name):
        if queue_name not in self.queues:
            raise ValueError(f"Queue with name {queue_name} does not exist.")
        if not self.queues[queue_name]:
            raise ValueError(f"Queue with name {queue_name} is empty.")
        else:
            queue_length = len(self.queues) 
            return queue_length 

    def toString(self):
        
        return str(self.queues)

