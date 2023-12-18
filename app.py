import uvicorn
from scripts.constants import app_configuration
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from scripts.core.handlers.sql_structure_handler import SqlData

sched = BlockingScheduler()
scheduler = BlockingScheduler(daemon=True)
load_dotenv()

if __name__ == '__main__':
    sql_data_obj = SqlData()
    uvicorn.run("main:app", host=app_configuration.HOST, port=int(app_configuration.PORT), workers=1)
    scheduler.add_job(sql_data_obj.fetch_data, CronTrigger.from_crontab('*/1 * * * *'), max_instances=1)
    while True:
        try:
            scheduler.start()
        except Exception as e:
            logger.error("Exception caught in the function : %s", str(e), exc_info=True)
