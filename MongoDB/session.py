from pymongo import MongoClient

def get_client(host: str="Localhost", port: int=27017):
    """Get a client for given host and port
    Default: Localhost, 27017"""
    return MongoClient(host, port)

def get_database(client: MongoClient, database_name: str):
    """Get requested database instance for given client"""
    return client[database_name]

def get_collection(database, collection_name: str):
    """Get collection from given database"""
    return database[collection_name]
