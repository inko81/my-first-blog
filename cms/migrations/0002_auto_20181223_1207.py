# Generated by Django 2.1.3 on 2018-12-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kintai',
            name='employee_no',
            field=models.IntegerField(verbose_name='社員No.'),
        ),
    ]