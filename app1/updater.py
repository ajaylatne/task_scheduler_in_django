from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import update_something


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', seconds=5)
    scheduler.start()
