from django.core.mail import send_mail
from news.settings import ADMIN_EMAIL
from celery import shared_task
from django.apps import apps


@shared_task
def send_async_message_reply(reply_id):
    model = apps.get_model(app_label='board', model_name='Reply')
    reply = model.objects.get(pk=reply_id)
    send_mail('Reply', 'You have another reply for your post', ADMIN_EMAIL,
              [reply.post.author.user.email])
    return 'message send success'
