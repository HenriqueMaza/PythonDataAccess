
from db_mongo import *;

class MongoDataAccessBase:
    dbMongo = None;
    collectionName = None;    

    def __init__(self, connectionString, collection):
        self.dbMongo = DBMONGO();
        self.dbMongo.connect(connectionString);
        self.collectionName = collection;
        pass;

    def getById(self, id):
        doc = self.dbMongo.findOne(self.collectionName,{'_id' : id})                
        return doc;      

    def insert(self, doc):
        self.dbMongo.insert(self.collectionName,doc);
        pass;

    def count(self, query):
        return self.dbMongo.count(self.collectionName,query);
        pass;

    def list(self, query):
        cursor = self.dbMongo.list(self.collectionName,query)
        responseDictionary = list(cursor);        
        return responseDictionary;              

    def listLimited(self, query, start, end):
        cursor = self.dbMongo.listLimited(self.collectionName,query,start,end)
        responseDictionary = list(cursor);        
        return responseDictionary; 

    def update(self, doc):
        self.dbMongo.update(self.collectionName,doc);
        pass;
        
    def dropAll(self):
        self.dbMongo.dropCollection(self.collectionName);
        pass;