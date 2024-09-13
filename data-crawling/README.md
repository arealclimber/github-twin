- [Data crawling](#data-crawling)
- [在本地端運行 MongoDB replica set](#在本地端運行-mongodb-replica-set)
  - [刪掉 mongodb 的資料 (Docker)](#刪掉-mongodb-的資料-docker)
  - [如果本地的 Python 連線 MongoDB cluster 失敗](#如果本地的-python-連線-mongodb-cluster-失敗)

# Data crawling

# 在本地端運行 MongoDB replica set

```bash
# Run docker compose
docker compose up -d

# Run the docker container and monitor the logs
docker-compose up --build

# Check the status of the containers
docker compose ps

# Check the logs of the containers
docker compose logs

# Connect to the main node of the MongoDB replica set to check if it's initiated
docker exec -it github-twin-mongo1 mongo --port 30001

# in mongodb shell, run:
rs.status()

# if there's error in `rs.status()`, initiate the replica set in the mongodb shell
rs.initiate({
  _id: "my-replica-set",
  members: [
    { _id: 0, host: "mongo1:30001" },
    { _id: 1, host: "mongo2:30002" },
    { _id: 2, host: "mongo3:30003" }
  ]
})

```

## 刪掉 mongodb 的資料 (Docker)

- 透過 `rs.status()` 可以看到主節點，如果要刪數據，需要將 table plus 連到主節點，才可以在 table plus 上刪除

  - 例如 `"syncSourceHost" : "mongo3:30003",`，代表 table plus 的 URL 需改成 `mongodb://localhost:30003`

- 進到 MongoDB 主節點，將所有 scrabble 的 posts table 資料刪掉

```bash
docker exec -it github-twin-mongo1 mongo --port 30001

# 查看主節點
rs.status()

# 如果主節點不是 30001 ，則需要切換到主節點，例如得知 `"syncSourceHost" : "mongo3:30003",`，則退出重新進 mongo3 的容器
exit
docker exec -it github-twin-mongo3 mongo --port 30003

# # 切換到主節點
# rs.switchToHost("mongo1:30001")

use scrabble
db.posts.deleteMany({})
```

- 刪除成功的話，會得到以下 log

```
my-replica-set:PRIMARY> use scrabble
switched to db scrabble
my-replica-set:PRIMARY> db.posts.deleteMany({})
{ "acknowledged" : true, "deletedCount" : 6901 }
```

## 如果本地的 Python 連線 MongoDB cluster 失敗

可能是主機名沒有在本地系統被正確配置

1. 在終端中，使用管理員權限編輯 /etc/hosts 文件：

```bash
sudo nano /etc/hosts
```

2. 在文件末尾添加以下行：

```bash
127.0.0.1 mongo1
127.0.0.1 mongo2
127.0.0.1 mongo3
```

把主機名 mongo1、mongo2 和 mongo3 映射到本地主機的 IP 地址（127.0.0.1）

3. 保存並關閉文件。在 nano 編輯器中，使用 Ctrl+X，然後按 Y 和 Enter 來保存更改。
4. 現在，嘗試 ping 這些主機名：

```bash
ping mongo1
ping mongo2
ping mongo3
```

能夠得到回覆，表明這些主機名現在可以解析為 127.0.0.1。

5. 再次運行 Python 腳本：

```bash
python insert_example.py
```

應該能得到 log：

```
Connected to MongoDB replica set:
Version: 5.0.28
Inserted document ID: 66dacabb54cf8ac496bb8ef2
```

並且能從 table plus 看到剛剛插入的資料
