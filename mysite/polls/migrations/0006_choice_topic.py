# Generated by Django 3.1.3 on 2022-07-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_topic2_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='topic',
            field=models.IntegerField(default=0),
        ),
    ]
