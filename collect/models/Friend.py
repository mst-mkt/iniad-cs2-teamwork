from django.db import models


class Friend(models.Model):
    user1 = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE, related_name="user1"
    )
    user2 = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE, related_name="user2"
    )
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user1", "user2"], name="unique_friendship")
        ]
        app_label = "collect"

    def __str__(self):
        return f"{self.user1} - {self.user2}"
