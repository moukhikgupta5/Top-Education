# Generated by Django 3.1.7 on 2021-03-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('fName', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('dob', models.DateField()),
            ],
        ),
    ]
