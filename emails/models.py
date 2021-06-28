from django.db import models
from django.conf import settings


class Email(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="sender_emails")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name="receiver_emails")

    is_read = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
