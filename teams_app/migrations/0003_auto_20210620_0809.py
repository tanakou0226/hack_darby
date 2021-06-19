# Generated by Django 3.2.4 on 2021-06-19 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams_app', '0002_auto_20210620_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='langs',
            field=models.ManyToManyField(blank=True, to='teams_app.Lang'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teams',
            name='techs',
            field=models.ManyToManyField(blank=True, to='teams_app.Tech'),
        ),
    ]