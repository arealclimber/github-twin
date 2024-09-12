import time
from pymongo import MongoClient
from datetime import datetime

def insert_data_to_mongodb(uri, database_name, collection_name, data):
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    
    try:
        result = collection.insert_one(data)
        print(f"Data inserted with _id: {result.inserted_id}, data: {data}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

def main():
    uri = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set"
    database_name = "scrabble"
    collection_name = "posts"

    try:
        while True:
            for _ in range(10):
                data = {
                    "platform": "github",
                    "content": "Test issue content",
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                }
                insert_data_to_mongodb(uri, database_name, collection_name, data)
            time.sleep(1)  # 每秒寫入 300 筆資料
    except KeyboardInterrupt:
        print("Data production stopped.")

if __name__ == "__main__":
    main()