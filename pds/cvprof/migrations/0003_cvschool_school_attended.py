# Generated by Django 4.1.4 on 2022-12-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvprof', '0002_cvlanguage_cvschool_cvskill_cvwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvschool',
            name='School_Attended',
            field=models.CharField(max_length=100, null=True),
        ),
    ]