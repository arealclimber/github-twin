from pymongo import MongoClient

# 連接到 MongoDB 副本集
# client = MongoClient("mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set")
client = MongoClient("mongodb://localhost:27017")

# 選擇數據庫和集合
db = client["mydatabase"]
collection = db["mycollection"]

# 插入示例數據
document = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
print("client in insert_example", client)
result = collection.insert_one(document)

print("Inserted document ID:", result.inserted_id)

# 關閉連接
client.close()