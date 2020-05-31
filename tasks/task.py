

from tasks.run import clearData

def add_task(scheduler=None,mysql=None):

    scheduler.add_job(clearData, 'cron',
                      hour=00,
                      minute=30,
                      second=00,
                      kwargs={
                          "db":mysql
                      })
if __name__ == '__main__':
    import sys,os
    from models.task import Cp
    PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)
    if PROJECT_PATH not in sys.path:
        sys.path.insert(0, PROJECT_PATH)

    # import json
    #
    # from tasks.cp import CpTaskBase
    # from models.cp import Cp
    # from loguru import logger

    add_task()