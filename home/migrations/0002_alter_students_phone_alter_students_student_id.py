# Generated by Django 4.0 on 2022-02-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.IntegerField(),
        ),
    ]
