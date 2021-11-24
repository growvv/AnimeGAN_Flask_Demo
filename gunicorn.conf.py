workers = 2    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整(多了没有，内存顶不住)
worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:8080"
timeout = 600  # 超时时间(必加)