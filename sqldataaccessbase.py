from db_mssql import *; 

class SQLDataAccessBase:
    connectionConfig = None
    dbMssql = None

    def __init__(self,config):
        self.connectionConfig = config
        self.dbMssql = DBMSSQL()
        self.dbMssql.connect(config['server'],
                             config['user'],
                             config['password'],
                             config['database'])
    pass

    def executeQuery(self, query):
        try:
            return self.dbMssql.executeQuery(query)
        except Exception as identifier:
            raise
        pass;
