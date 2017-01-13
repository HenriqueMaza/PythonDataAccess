#!/usr/bin/python
import pymssql

class DBMSSQL:
    connection = None;

    def connect(self,server,user,password,database):
        self.connection = pymssql.connect(server, user, password, database);

    def executeQuery(self,query):        
        cursor = self.connection.cursor(as_dict=True)
        cursor.execute(query);
        return cursor.fetchall();
        pass;