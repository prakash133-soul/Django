# Generated by Django 3.2.4 on 2021-06-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=120)),
                ('Address', models.CharField(max_length=120)),
                ('Firstname', models.CharField(max_length=120)),
                ('Lastname', models.CharField(max_length=120)),
            ],
        ),
    ]
