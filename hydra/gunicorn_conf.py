import multiprocessing
import os

workers = max(2, multiprocessing.cpu_count() * 2 + 1)
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 90
graceful_timeout = 30
accesslog = "-"
errorlog = "-"
loglevel = os.getenv("LOGLEVEL", "info")
