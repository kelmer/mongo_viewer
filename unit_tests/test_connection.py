'''
Created on Sep 8, 2012

@author: kelmer
'''
import unittest
import connection

class TestConnection(unittest.TestCase):


    def testConnection(self):
        new_con = connection.get_connection()
        self.assert_(type(new_con)==connection.Connection, 'this is not as pymongo object')
           
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()