# Generated by Django 3.1.3 on 2022-07-11 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_topic2'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic2',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
