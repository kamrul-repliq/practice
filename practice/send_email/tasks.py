from django.contrib.auth import get_user_model

from celery import shared_task

from .send_email_message import send_email


@shared_task(bind=True)
def send_email_func(self):
    users = get_user_model().objects.filter()

    for user in users:
        mail_subject = "Hi Celery Testing."
        message = f"Hello {user.username} How Are you?"
        to_email = user.email
        send_email(mail_subject, message, to_email)

    return "Done!"
