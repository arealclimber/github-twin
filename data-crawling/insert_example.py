# # from pymongo import MongoClient

# # # 連接到 MongoDB 副本集
# # # client = MongoClient("mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set")
# # client = MongoClient("mongodb://localhost:27017")
# # # client = MongoClient("mongodb://localhost:30001")

# # # 選擇數據庫和集合
# # db = client["mydatabase"]
# # collection = db["mycollection"]

# # # 插入示例數據
# # document = {
# #     "name": "John Doe",
# #     "age": 1610,
# #     "city": "New York"
# # }
# # print("client in insert_example", client)
# # result = collection.insert_one(document)

# # print("Inserted document ID:", result.inserted_id)

# # # 關閉連接
# # client.close()


# # # ----

# from pymongo import MongoClient

# # 連接到 MongoDB 副本集
# # client = MongoClient("mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set")
# client = MongoClient("mongodb://localhost:30001")

# # 選擇數據庫和集合
# db = client["mydatabase"]
# collection = db["mycollection"]

# # 插入示例數據
# document = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }
# print("client in insert_example", client)
# result = collection.insert_one(document)

# print("Inserted document ID:", result.inserted_id)

# # 關閉連接
# client.close()


from pymongo import MongoClient

# 連接到 MongoDB 副本集
client = MongoClient("mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set")

try:
    # 檢查連接
    server_info = client.server_info()
    print("Connected to MongoDB replica set:")
    print(f"Version: {server_info['version']}")

    # 選擇數據庫和集合
    db = client["mydatabase"]
    collection = db["mycollection"]

    # 插入示例數據
    document = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    result = collection.insert_one(document)

    print("Inserted document ID:", result.inserted_id)

except Exception as e:
    print("Error connecting to MongoDB replica set:")
    print(e)

finally:
    # 關閉連接
    client.close()