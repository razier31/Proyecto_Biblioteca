# Generated by Django 4.2.1 on 2023-06-02 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0017_alter_prestamolibro_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_devolucion',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 4, 19, 19, 50, 337235, tzinfo=datetime.timezone.utc)),
        ),
    ]
