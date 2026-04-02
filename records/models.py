from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class FinancialRecord(models.Model):
    class RecordType(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="records"
    )

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    type = models.CharField(
        max_length=10,
        choices=RecordType.choices
    )

    category = models.CharField(max_length=100)

    date = models.DateField()

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.amount} ({self.user})"