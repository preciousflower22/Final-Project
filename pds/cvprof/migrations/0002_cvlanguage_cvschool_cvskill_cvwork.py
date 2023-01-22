# Generated by Django 4.1.4 on 2022-12-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvprof', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primarylang', models.CharField(max_length=255)),
                ('secondarylang', models.CharField(max_length=500)),
                ('tertiarylang', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CVSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.CharField(max_length=255)),
                ('secondary', models.CharField(max_length=500)),
                ('tertiary', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CVSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstski', models.CharField(max_length=255)),
                ('secondski', models.CharField(max_length=500)),
                ('tertiaryski', models.CharField(max_length=254)),
                ('specialize', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CVWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstjob', models.CharField(max_length=255)),
                ('secondjob', models.CharField(max_length=500)),
                ('tertiaryjob', models.CharField(max_length=254)),
            ],
        ),
    ]