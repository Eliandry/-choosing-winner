# Generated by Django 3.1.1 on 2020-10-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choiceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]