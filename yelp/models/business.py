from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Business(models.Model):
    business_id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    stars = models.FloatField()
    review_count = models.PositiveIntegerField(default=0)
    is_open = models.PositiveIntegerField(default=0)
    attributes = models.JSONField(null=True)
    categories = ArrayField(models.TextField(null=True, blank=True), null=True, blank=True)
    hours = models.JSONField(null=True)

    class Meta:
        db_table = "business"