# Generated by Django 3.1 on 2020-08-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickynote',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
