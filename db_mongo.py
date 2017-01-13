#!/usr/bin/python
from pymongo import *

class DBMONGO:

    connection = None;
    database = None;

    def connect(self,connectionString):
        self.connection = MongoClient(connectionString) 
        self.database = self.connection.get_default_database()

    def insert(self,collectionName,doc):
        try:
            collection = self.database.get_collection(collectionName)
            collection.insert_one(doc)
        except Exception as identifier:
            raise
        pass;

    def update(self,collectionName,doc):
        try:
            collection = self.database.get_collection(collectionName)
            query = {'_id' : doc['_id']};
            collection.find_and_modify(query,doc,True)
        except Exception as identifier:
            raise
        pass;

    def list(self,collectionName,query):
        try:
            collection = self.database.get_collection(collectionName)
            return collection.find(query)   
        except Exception as identifier:
            raise
        pass;
    
    def listLimited(self,collectionName,query,skip,max):
        try:
            collection = self.database.get_collection(collectionName)
            return collection.find(query).skip(skip).limit(max) 
        except Exception as identifier:
            raise
        pass;

    def count(self,collectionName,query):
        try:
            collection = self.database.get_collection(collectionName)
            return collection.count(query)
        except Exception as identifier:
            raise
        pass;

    def findOne(self,collectionName,query):
        try:
            collection = self.database.get_collection(collectionName)
            return collection.find_one(query) 
        except Exception as identifier:
            raise
        pass;
    
    def dropCollection(self,collectionName):
        try:
            self.database.drop_collection(collectionName)
        except Exception as identifier:
            raise
        pass;

    def executeQuery(self,query):
        try:
            self.database.get_collection(collectionName)
            return collection.find(query)  
        except Exception as identifier:
            raise        
        pass;