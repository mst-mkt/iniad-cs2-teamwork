from django.db import models


class Notification(models.Model):
    """通知テーブル"""

    title = models.CharField(max_length=100)
    text = models.TextField()
    posted_at = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "collect"
