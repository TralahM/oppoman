from django.db import models
from bsct.models import BSCTModelMixin

# Create your models here.


class Account(models.Model, BSCTModelMixin):
    username = models.CharField(max_length=95, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    @classmethod
    def get_allowed_fields(cls):
        return [
            "username",
            "address",
        ]

    def __str__(self):
        return f"{self.username}"


class Opportunity(models.Model, BSCTModelMixin):
    CHOICES = (
        ("DISCOVERY", "DISCOVERY"),
        ("PROPOSAL_SHARED", "PROPOSAL_SHARED"),
        ("NEGOTIATIONS", "NEGOTIATIONS"),
    )
    name = models.CharField(max_length=95)
    account = models.ForeignKey(
        "opportunities.Account",
        null=True,
        to_field="username",
        on_delete=models.CASCADE,
    )
    amount = models.FloatField()
    stage = models.CharField(max_length=58, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    @classmethod
    def get_allowed_fields(cls):
        return [
            "name",
            "account",
            "amount",
            "stage",
        ]

    def __str__(self):
        return f"{self.name}"
