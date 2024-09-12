from pymongo import MongoClient

def clear_posts():
    uri = "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set"
    client = MongoClient(uri)
    db = client["scrabble"]
    collection = db["posts"]

    # 刪除所有資料
    result = collection.delete_many({})
    print(f"刪除的文件數量: {result.deleted_count}")

if __name__ == "__main__":
    clear_posts()