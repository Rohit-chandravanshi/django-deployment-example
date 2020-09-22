# Generated by Django 3.1.1 on 2020-09-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=260)),
                ('email', models.URLField(unique=True)),
            ],
        ),
    ]
