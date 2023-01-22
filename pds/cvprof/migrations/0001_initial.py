# Generated by Django 4.1.4 on 2022-12-20 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]