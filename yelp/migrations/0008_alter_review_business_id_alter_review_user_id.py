# Generated by Django 4.1.2 on 2022-11-02 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yelp', '0007_yelpuser_elite_yelpuser_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='business_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='yelp.business'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='yelp.yelpuser'),
        ),
    ]
