# Generated by Django 4.2.2 on 2023-07-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactiontime',
            name='game',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]