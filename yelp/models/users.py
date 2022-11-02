from django.db import models

# Create your models here.
class YelpUser(models.Model):
    user_id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=100)
    review_count = models.PositiveIntegerField(default=0)
    yelping_since = models.DateTimeField()
    friends = models.TextField(null=True, blank=True)
    useful = models.PositiveIntegerField(default=0)
    funny = models.PositiveIntegerField(default=0)
    cool = models.PositiveIntegerField(default=0)
    fans = models.PositiveIntegerField(default=0)
    elite = models.TextField(null=True, blank=True)
    average_stars = models.FloatField()    
    compliment_hot = models.PositiveIntegerField(default=0)
    compliment_more = models.PositiveIntegerField(default=0)
    compliment_profile = models.PositiveIntegerField(default=0)
    compliment_cute = models.PositiveIntegerField(default=0)
    compliment_list = models.PositiveIntegerField(default=0)
    compliment_note = models.PositiveIntegerField(default=0)
    compliment_plain = models.PositiveIntegerField(default=0)
    compliment_cool = models.PositiveIntegerField(default=0)
    compliment_funny = models.PositiveIntegerField(default=0)
    compliment_writer = models.PositiveIntegerField(default=0)
    compliment_photos = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "users"