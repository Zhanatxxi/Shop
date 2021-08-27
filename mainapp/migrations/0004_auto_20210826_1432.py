# Generated by Django 3.0.8 on 2021-08-26 14:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
