# Generated by Django 3.2.16 on 2023-01-10 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_detailfakturpenjualan_kuantitas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]
