# Generated by Django 3.0.6 on 2020-05-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='mobile',
            field=models.CharField(default='', max_length=20),
        ),
    ]