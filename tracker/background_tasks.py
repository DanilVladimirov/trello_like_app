from email_sender.factory import EmailSenderFactory
from email_sender.constants import EmailTypes

from tracker.models import Task


async def send_task_change_email(task: Task):
    owner_email = task.owner.email
    data = {"task_name": task.name}

    await EmailSenderFactory.get_sender().send(data=data, email_type=EmailTypes.TASK_UPDATED, recipients=[owner_email])
