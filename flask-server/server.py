from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv(""))

database = os.environ.get("MONGODB_PWD")

connection_string = database

client = MongoClient(connection_string)

dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()


def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Justin",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)


production = client.production
person_collection = production.person_collection


def create_documents():
    first_name = ["Stevie", "Billy", "Hughie"]
    last_name = ["Vaughan", "Butcher", "Campbell"]
    ages = [65, 32, 45]

    docs = []

    for first_name, last_name, age in zip(first_name, last_name, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)

    person_collection.insert_many(docs)


printer = pprint.PrettyPrinter()


def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)


def find_billy():
    billy = person_collection.find_one({"first_name": "Billy"})
    printer.pprint(billy)


def count_all_people():
    count = person_collection.count_documents(filter={})
    print("Number of people", count)


def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)

get_person_by_id("62ace4e051bcb4dfb17b9de1")