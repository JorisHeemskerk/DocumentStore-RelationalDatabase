from pymongo import MongoClient

def getClient(host: str="Localhost", port: int=27017):
    """Get a client for given host and port
    Default: Localhost, 27017"""
    return MongoClient(host, port)

def getDatabase(client: MongoClient, database_name: str):
    """Get requested database instance for given client"""
    return client[database_name]

def getCollection(database, collection_name: str):
    """Get collection from given database"""
    return database[collection_name]
