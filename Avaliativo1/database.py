from typing import Collection
import pymongo

class Database:
    def __init__(self, database):
        self.connect(database)

    def connect(self, database):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def disconnect(self):
        self.clusterConnection.close()
        print("Database disconnected successfully!")

    def create_collection(self, collection_name, validator=None):
        try:
            self.collection = self.db.create_collection[collection_name, validator]
            print("Collection created successfully!")
        except Exception as e:
            print(e)

    