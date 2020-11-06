from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# from django.urls import reverse
from bsct.models import BSCTModelMixin

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """ Create and Save a User with given username and password """
        if not username:  # pragma no cover
            raise ValueError("username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular User with the given username and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        # extra_fields.setdefault('confirmed_at', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given username and password.""" ""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:  # pragma no cover
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:  # pragma no cover
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username, password, **extra_fields)


class User(AbstractUser, BSCTModelMixin):
    username = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "username"
    objects = UserManager()

    @classmethod
    def get_allowed_fields(cls):
        return ["username", "password"]
