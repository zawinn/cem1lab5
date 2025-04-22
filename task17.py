from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  
db = client['myshinynewdb'] 
collection = db['user'] 

new_document = {
    "name": "Ada Lovelace",
    "age": 205
}

result = collection.insert_one(new_document)

print(f"Новый документ вставлен с ID: {result.inserted_id}")
