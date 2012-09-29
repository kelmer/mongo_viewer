'''
Created on Sep 8, 2012

@author: kelmer
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_main
import connection
con = None


class MainWindow(QMainWindow,ui_main.Ui_MainWindow):
    
    def __init__(self, parent = None):
        
        super(MainWindow,self).__init__(parent)
        self.showMaximized()
        self.setupUi(self)
        self.connect(self.actionNew_Database,SIGNAL("triggered()"), self.add_db)
        self.connect(self.pushButtonConnect, SIGNAL("clicked()"), self.get_connection)
      
    def add_db(self):
	''' adds a new database in MongoDB '''        
        con = connection.get_connection()
        db_names = con.database_names()
        self.textEdit.setText("Existing Databases:\n" + '\n'.join([i for i in db_names]))


    def get_connection(self):
        '''
        gets a connection to the mongodb server.
        '''
        host = unicode(self.lineEditHost.text())
        port = unicode(self.lineEditPort.text())

        if len and host:
            try:
                global con
                con = connection.get_connection(unicode(host), int(port))
                self.plainTextEditQueries.insertPlainText("Connected Successfully to MongoDB at " + '<' + con.host + '>')
                self.plainTextEditQueries.appendPlainText('Write your Pythonic query here...\n')
                
            except:
                self.plainTextEditQueries.insertPlainText("A problem has ocurred, no connection to MongoDB!")

        else:

            try:

                global con 
                con = connection.get_connection()
                self.plainTextEditQueries.insertPlainText("Connected Successfully to MongoDB at " + '<' + con.host + '>')
                self.plainTextEditQueries.appendPlainText('Write your Pythonic query here...\n')
                
            
                
            #self.connect(self.treeWidgetMain, SIGNAL("activated"), self.activated)

            except:
                self.plainTextEditQueries.insertPlainText("A problem has ocurred, no connection to MongoDB!")
        
        self.populate_main_tree()

    def populate_main_tree(self):
        '''
        populates the main treewidget with the databases in mongodb
        '''
        dbs = con.database_names() #returns a list with the database names
        cols = {} # collection names
        for i in dbs:
            if i not in cols:
                db = con[i]
                cols[i] = db.collection_names()

        
        self.treeWidgetMain.clear()
        self.treeWidgetMain.setColumnCount(2)
        headers = ['Databases / Collections']
        self.treeWidgetMain.setHeaderLabels(headers)
        self.treeWidgetMain.setItemsExpandable(True)
        for i in cols:
            iten = QTreeWidgetItem(self.treeWidgetMain, [i])
            icon = QIcon()
            icon.addPixmap(QPixmap(":/images/images/database.png"), QIcon.Normal, QIcon.Off)
            iten.setIcon(0,icon)
            #self.treeWidgetMain.expandItem(iten)            
            for j in cols.get(i):
                sub_iten = QTreeWidgetItem(iten, [j])
                sub_icon = QIcon()
                sub_icon.addPixmap(QPixmap(":/images/images/collection.png"), QIcon.Normal, QIcon.Off)
                sub_iten.setIcon(0,sub_icon)
                #self.treeWidgetMain.expandItem(sub_iten)

        

        #iten.setTextAlignment(1, Qt.AlignRight|Qt.AlignVCenter)        



        


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
