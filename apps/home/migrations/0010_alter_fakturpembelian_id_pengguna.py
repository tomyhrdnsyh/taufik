# Generated by Django 3.2.16 on 2022-11-15 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_fakturpembelian_id_pengguna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakturpembelian',
            name='id_pengguna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='pengguna'),
        ),
    ]
