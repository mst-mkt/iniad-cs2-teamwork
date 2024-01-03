from django.conf import settings
from django.db import models


class Message(models.Model):
    """メッセージテーブル"""

    text = models.TextField()
    posted_at = models.DateField()
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    def __str__(self):
        return self.text

    class Meta:
        app_label = "collect"
