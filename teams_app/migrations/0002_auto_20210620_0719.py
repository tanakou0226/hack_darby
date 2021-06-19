# Generated by Django 3.2.4 on 2021-06-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='lang',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='teams',
            name='techs',
            field=models.ManyToManyField(to='teams_app.Tech'),
        ),
    ]
