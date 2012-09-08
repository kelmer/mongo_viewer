'''
Created on Sep 8, 2012

@author: kelmer
'''
import pymongo
from pymongo import Connection

class Connection(object):
    '''
    creates a connection object to connect to MongoDB
    '''


    def __init__(self, host='localhost', port='27017'):
        '''
        connects to MongoDB with host and port parameters
        if no host or port, default values apply
        '''
        self.host = host
        self.port = port
        self.con = Connection()

    def get_host(self):
        ''' gets a host address'''
        return self.__host


    def get_port(self):
        ''' gets a port number'''
        return self.__port


    def set_host(self, value):
        ''' sets a new host '''
        self.__host = value


    def set_port(self, value):
        ''' sets a new port '''
        self.__port = value


    def del_host(self):
        ''' deletes the current host '''
        del self.__host


    def del_port(self):
        ''' deletes the current port '''
        del self.__port

    host = property(get_host, set_host, del_host, "it's the address hosting the system")
    port = property(get_port, set_port, del_port, "it's the port MongoDB use to communicate")
    
    
        
        
        