'''
Created on Sep 8, 2012

@author: kelmer
'''
import unittest
import connection

class TestConnection(unittest.TestCase):


    def testConnection(self):
        new_con = connection.Connection()
        print new_con.host
        
        new_con.set_host()
        print new_con.host
        self.assert_(type(new_con.host)==str, 'this is not a string!')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()