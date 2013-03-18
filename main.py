'''
Created on Sep 8, 2012

@author: kelmer
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_main
import connection
from bson import ObjectId
from ast import literal_eval


ROW_LIMIT = 1000 # this is provisional just to try speed



class MainWindow(QMainWindow,ui_main.Ui_MainWindow):
    
    def __init__(self, parent = None):
        
        super(MainWindow,self).__init__(parent)
        self.con = None
        self.db = None
        self.col = None
        self.showMaximized()
        self.setupUi(self)
        self.connect(self.actionNew_Collection,SIGNAL("triggered()"), self.add_collection)
        self.connect(self.actionRun_Query,SIGNAL("triggered()"), self.run_query)
        self.connect(self.pushButtonConnect, SIGNAL("clicked()"), self.get_connection)
        self.connect(self.treeWidgetMain, SIGNAL("itemClicked (QTreeWidgetItem *,int)"), self.get_collection)
      
    def add_collection(self):
	''' adds a new collection in MongoDB '''        
        pass
        #con = connection.get_connection()
        #col_names = con.database_names()
        #self.plainTextEditQueries.clear()
        #self.plainTextEditQueries.insertPlainText("Existing Databases:\n" + '\n'.join([i for i in db_names]))


    def get_connection(self):
        '''
        gets a connection to the mongodb server.
        '''
        host = unicode(self.lineEditHost.text())
        port = unicode(self.lineEditPort.text())
        self.plainTextEditQueries.clear()

        if len and host:
            try:
                
                self.con = connection.get_connection(unicode(host), int(port))
                self.plainTextEditQueries.insertPlainText("Connected Successfully to MongoDB at " + '<' + self.con.host + '>')
                self.plainTextEditQueries.appendPlainText('Write your Pythonic query here...\n')
                
            except:
                font = QFont()
                font.setUnderline(True)
                self.plainTextEditQueries.setFont(font)
                self.plainTextEditQueries.insertPlainText("A problem has ocurred, no connection to MongoDB!")

        else:

            try:

                self.con = connection.get_connection()
                self.plainTextEditQueries.insertPlainText("Connected Successfully to MongoDB at " + '<' + self.con.host + '>')
                self.plainTextEditQueries.appendPlainText('Write your Pythonic query here...\n')
                      

            except:
                self.plainTextEditQueries.insertPlainText("A problem has ocurred, no connection to MongoDB!")
        
        self.populate_main_tree()

    def get_collection(self):
        '''
        gets a collection when the user selects a item in the treewidget
        '''
        self.textEditMain.clear()
        item = self.treeWidgetMain.currentItem()
        if item.parent() != None: #which means the item is already a collection
            
            self.db = self.con[unicode(item.parent().text(0))]
            self.col = self.db[unicode(item.text(0))]
                
            self.populate_text()
            self.populate_main_table()

        else:
            try:
                del(self.col)                    
                self.db = self.con[unicode(item.text(0))]
            except:
                self.db = self.con[unicode(item.text(0))]

    def populate_main_tree(self):
        '''
        populates the main treewidget with the databases in mongodb
        '''
        dbs = self.con.database_names() #returns a list with the database names
        cols = {} # collection names
        for i in dbs:
            if i not in cols:
                db = self.con[i]
                cols[i] = db.collection_names()

        
        self.treeWidgetMain.clear()
        self.treeWidgetMain.setColumnCount(2)
        headers = ['Databases / Collections']
        self.treeWidgetMain.setHeaderLabels(headers)
        self.treeWidgetMain.setItemsExpandable(True)
        for i in cols:
            item = QTreeWidgetItem(self.treeWidgetMain, [i])
            icon = QIcon()
            icon.addPixmap(QPixmap(":/images/images/database.png"), QIcon.Normal, QIcon.Off)
            item.setIcon(0,icon)                        
            for j in cols.get(i):
                sub_item = QTreeWidgetItem(item, [j])
                sub_icon = QIcon()
                sub_icon.addPixmap(QPixmap(":/images/images/collection.png"), QIcon.Normal, QIcon.Off)
                sub_item.setIcon(0,sub_icon)

    def populate_text(self):
        '''
        populates the textEditMain field with the data from self.collection
        '''
        for i in self.col.find().limit(1000):                
                self.textEditMain.append(unicode(i))

    def populate_main_table(self):
        '''
        populates the main table with the data of the collection selected
        to preserve memory it limits the rows to 1000
        '''
        headers = [i for i in self.col.find_one()]
        self.tableWidgetMain.clear()
        self.tableWidgetMain.setSortingEnabled(False)

        self.tableWidgetMain.setColumnCount(len(headers))
        self.tableWidgetMain.setHorizontalHeaderLabels(headers)
        self.tableWidgetMain.setRowCount(ROW_LIMIT)
        # the ROW COUNT above if there is not a LIMIT SHOULD BE CHANGED TO:
        #self.col.find().limit(1000).count()
                
        row = 0
        column = 0
        
        for j in self.col.find().limit(1000):            
            for i in j:
                if i in headers:
                    self.tableWidgetMain.setItem(row, headers.index(i), QTableWidgetItem(unicode(j[i])))
                
                else:                    
                    headers.append(i)
                    self.tableWidgetMain.setColumnCount(len(headers))
                    self.tableWidgetMain.setHorizontalHeaderLabels(headers)
                    self.tableWidgetMain.setItem(row, headers.index(i), QTableWidgetItem(unicode(j[i])))
            row +=1


        self.tableWidgetMain.setSortingEnabled(True)

    def run_query(self):
        '''
        run the pymongo query introduced in the plainTextEditQueries
        '''
        query = unicode(self.plainTextEditQueries.toPlainText())
        print self.col.find(literal_eval(query)).count()
        




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
