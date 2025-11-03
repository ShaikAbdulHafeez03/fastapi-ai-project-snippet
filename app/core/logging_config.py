# import logging
# import sys
# from pythonjsonlogger import jsonlogger
# from contextvars import ContextVar
# import threading
# import queue
# import time
# import json
# import requests



# # Loki batch sender (simple synchronous background worker).
# class LokiBatchHandler(logging.Handler):
#     def __init__(self, loki_url, batch_size=50, flush_interval=2, timeout=2):
#         super().__init__()
#         self.loki_url = loki_url
#         self.batch_size = batch_size
#         self.flush_interval = flush_interval
#         self.timeout = timeout
#         self.q = queue.Queue(maxsize=10000)
#         self._stop = threading.Event()
#         self.worker = threading.Thread(target=self._worker, daemon=True)
#         self.worker.start()

#     def emit(self, record):
#         try:
#             msg = self.format(record)
#             self.q.put_nowait(msg)
#         except queue.Full:
#             pass

#     def _worker(self):
#         buffer = []
#         while not self._stop.is_set():
#             try:
#                 item = self.q.get(timeout=self.flush_interval)
#                 buffer.append(item)
#             except Exception:
#                 pass

#             if len(buffer) >= self.batch_size or (buffer and self._stop.is_set()):
#                 # prepare stream
#                 streams = [
#                     {
#                         "stream": {"job": "fastapi-app"},
#                         "values": [[str(int(time.time() * 1e9)), json.dumps({"log": b})] for b in buffer]
#                     }
#                 ]
#                 payload = {"streams": streams}
#                 try:
#                     requests.post(self.loki_url, json=payload, timeout=self.timeout)
#                 except Exception:
#                     # fallback or drop
#                     pass
#                 buffer = []

#     def close(self):
#         self._stop.set()
#         self.worker.join(timeout=1)
#         super().close()

# def get_logger(name="fastapi-app", level=logging.INFO, loki_url=None):
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     if logger.handlers:
#         return logger

#     fmt = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s %(request_id)s %(user_id)s')
#     sh = logging.StreamHandler(sys.stdout)
#     sh.setFormatter(fmt)
#     logger.addHandler(sh)

#     if loki_url:
#         lh = LokiBatchHandler(loki_url=loki_url)
#         lh.setFormatter(fmt)
#         logger.addHandler(lh)

#     return logger
