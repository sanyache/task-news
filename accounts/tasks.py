from django.core.mail import get_connection

from celery import shared_task


@shared_task(rety_backoff=True, serializer="pickle")
def async_send_messages(email_messages):
    conn = get_connection(backend='django.core.mail.backends.smtp.EmailBackend')
    conn.send_messages(email_messages)
