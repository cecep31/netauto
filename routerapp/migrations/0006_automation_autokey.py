# Generated by Django 3.1.7 on 2021-03-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routerapp', '0005_auto_20210324_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='autokey',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]