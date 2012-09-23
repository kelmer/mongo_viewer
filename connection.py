'''
Created on Sep 8, 2012

@author: kelmer
'''
import pymongo
from pymongo import Connection


def get_connection(host="localhost", port=27017):
    
    con = Connection(host, port)
    return con

    
    
        
        
        