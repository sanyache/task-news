from django.core.mail.backends.base import BaseEmailBackend
from accounts.tasks import async_send_messages


class CustomEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        async_send_messages.delay(email_messages)
        return len(email_messages)