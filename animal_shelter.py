#Ryan Kittelson
#CS-340
#Project One
#CRUD - Create, Read, Update, Delete


from pymongo import MongoClient

from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # init to connect to mongoDB without authentication
        #self.client = MongoClient('mongodb://localhost:47921')
        # init to connect to mongoDB with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:47921/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary   
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read_all(self, data):
        cursor = self.database.animals.find(data,{'_id':False})
        return cursor
    
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data) # returns one document in python library
        else:
            print("Nothing to read, because data parameter is empty")
            return False
        
    def update_one(self, data):
        if data is not None:
            return self.database.animals.updateOne(data) # update one document in python library
        else:
            print("Nothing to update, because data parameter is empty")
            return False
    
    def update_many(self, data):
        if data is not None:
            return self.database.animals.updateMany(data) # updates many documents in python library
        else:
            print("Nothing to update, because data parameter is empty")
            return False
        
    def replace_one(self, data):
        if data is not None:
            return self.database.animals.replaceOne(data) # replaces one document in python library
        else:
            print("Nothing to replace, because data parameter is empty")
            return False
        
    def delete_one(self, data):
        if data is not None:
            return self.database.animals.deleteOne(data) # deletes one document in python library
        else:
            print("Nothing to delete, because data parameter is empty")
            return False

    def delete_many(self, data):
        if data is not None:
            return self.database.animals.deleteMany(data) # deletes many document in python library that satisfy given critera
        else:
            print("Nothing to delete, because data parameter is empty")
            return False