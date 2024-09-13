- [Data ingestion](#data-ingestion)
  - [檢查 rabbitmq 的情況 (Docker)](#檢查-rabbitmq-的情況-docker)

# Data ingestion

## 檢查 rabbitmq 的情況 (Docker)

- 執行 `docker compose up -d` 後，可以在 `http://localhost:15673` 看到 rabbitmq 的 web ui，根據 data-ingestion/config.py 的 RABBITMQ_DEFAULT_USERNAME 和 RABBITMQ_DEFAULT_PASSWORD 登入後，可以看到 queue 的狀況

- 進到運行 RabbitMQ 的 container `docker exec -it <rabbitmq-container-name> bash`

```bash
docker exec -it github-twin-mq bash
```

```bash
# 查看 queue
rabbitmqctl list_queues

# 查看 rabbitmq 的 status
rabbitmqctl status

# 查看 rabbitmq 的 cluster 的 status
rabbitmqctl cluster_status

# 查看 rabbitmq 的連線
rabbitmqctl list_connections

# 查看 rabbitmq 的節點
rabbitmqctl node_health_check

# 查看 rabbitmq 的消費者
rabbitmqctl list_consumers

# 查看 rabbitmq 的 vhost
rabbitmqctl list_vhosts
```

- 清空 queue `rabbitmqctl purge_queue <queue-name>`

```bash
rabbitmqctl purge_queue default
```
