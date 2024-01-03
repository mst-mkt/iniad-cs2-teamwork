import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core import validators
from django.db import models


class CustomUserManager(BaseUserManager):
    """カスタムユーザーマネージャー"""

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        normalized_email = self.normalize_email(email)
        user = self.model(username=username, email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        return self._create_user(username, email, password, **extra_fields)

    class Meta:
        app_label = "collect"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=16,
        unique=True,
        validators=[
            validators.RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Username must be Alphanumeric or contain Underscore",
            )
        ],
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    profile = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    display_name = models.CharField(max_length=24, blank=True, default="")
    links = models.JSONField(default=list)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=30, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        app_label = "collect"
