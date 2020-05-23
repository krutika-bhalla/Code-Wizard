import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.users = self.db.users

    def insert_user(self,data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

        id = self.users.insert({"username": data.username, "name": data.name, "password": hashed, "email":data.email})

        print("User-Id is: ", id)
        myuser = self.users.find_one({"username": data.username})

        if bcrypt.checkpw("123123".encode(), myuser["password"]):
            print("Matches")