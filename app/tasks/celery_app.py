# from celery import Celery
# from app.config import settings
# import time

# celery = Celery('tasks', broker=settings.CELERY_BROKER_URL, backend=settings.CELERY_RESULT_BACKEND)

# @celery.task(bind=True)
# def long_running_task(self, payload):
#     # Simulate long task with progress updates
#     total = 10
#     for i in range(total):
#         time.sleep(1)
#         self.update_state(state='PROGRESS', meta={'progress': int((i+1)/total*100)})
#     return {"result": "done", "payload": payload}
