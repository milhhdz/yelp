from django.db import models
from django.contrib.postgres.fields import ArrayField

from yelp.models.users import YelpUser
from yelp.models.business import Business

# Create your models here.
class Review(models.Model):
    review_id = models.CharField(max_length=22, primary_key=True)
    user_id = models.ForeignKey(
        YelpUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    business_id = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    stars = models.FloatField(default=0)
    date = models.DateTimeField()
    text = models.TextField()
    useful = models.PositiveIntegerField(default=0)
    funny = models.PositiveIntegerField(default=0)
    cool = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "reviews"