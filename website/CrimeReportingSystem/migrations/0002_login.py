# Generated by Django 3.1.4 on 2020-12-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrimeReportingSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
