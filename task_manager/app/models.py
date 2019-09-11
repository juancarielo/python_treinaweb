from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('A', 'Alta'),
        ('N', 'Normal'),
        ('B', 'Baixa'),
    ]
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    date_expiration = models.DateField(null=False, blank=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, null=False, blank=False)