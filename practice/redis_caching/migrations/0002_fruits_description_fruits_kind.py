# Generated by Django 4.2 on 2023-05-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redis_caching', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fruits',
            name='kind',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]