import requests
from SERVER_CONFIG import SERVER_ADDRESS, SERVER_PORT
from apscheduler.schedulers.background import BackgroundScheduler
from Scheduler_color import ServiceScheduler
from init import create_app

req = requests.get("https://raw.githubusercontent.com/BulRUSSIA/protected.github.io/master/test")
print(req.text)
print(type(req.text))
response = req.text[0]
if response == "1":
    print("accsess true7")
    app = create_app()
    JOB = ServiceScheduler()
    scheduler = BackgroundScheduler()
    scheduler.add_job(JOB.auto_admin, trigger='interval', seconds=5)
    #scheduler.add_job(JOB.check_banned, trigger='interval', seconds=5)
    scheduler.add_job(JOB.avatar, trigger='interval', seconds=2.5)
    #scheduler.add_job(JOB.scheduled_message_add_cash, trigger='interval', seconds=20)
    scheduler.add_job(JOB.attachments_banned, trigger='interval', seconds=1.5)
    scheduler.add_job(JOB.combine_avatar_lists, trigger='interval', seconds=5)
    scheduler.start()
else:
    print("accsess denied")



if __name__ == '__main__':
    app.run(port=SERVER_PORT, host=SERVER_ADDRESS)  # 79.174.12.77
