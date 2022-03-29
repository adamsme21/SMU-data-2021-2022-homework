import pymongo
from scrape_mars import ScrapingHelper

class MongoHelper():
    def __init__(self):
        # Create connection variable
        self.conn = 'mongodb://localhost:27017'

        # Pass connection to pymongo instance.
        self.engine = pymongo.MongoClient(self.conn)

        # Connect/create to a database.
        self.db = self.engine.mars_db

    def insertData(self, data):
        self.db.mars_data.drop()

        self.db.mars_data.insert_many(
            [
                data
            ]
        )

        return({"ok": True})