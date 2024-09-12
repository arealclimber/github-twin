from pymongo import MongoClient
from datetime import datetime



def insert_data_to_mongodb(uri, database_name, collection_name, data):
    """
    Insert data into a MongoDB collection.

    :param uri: MongoDB URI
    :param database_name: Name of the database
    :param collection_name: Name of the collection
    :param data: Data to be inserted (dict)
    """
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    current_time = datetime.now().strftime("%H:%M:%S")
    data["timestamp"] = current_time

    try:
        result = collection.insert_one(data)
        print(f"Data inserted with _id: {result.inserted_id}, data: {data}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    insert_data_to_mongodb(
        "mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set",
        "scrabble",
        "posts",
        {"platform": "github", "content": "Test content"}
    )
