# Generated by Django 4.0.2 on 2022-02-14 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_refdata_dataset_alter_refdata_ref_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='refdata',
            name='latest_date',
            field=models.DateField(default=datetime.date(2022, 2, 14)),
            preserve_default=False,
        ),
    ]
