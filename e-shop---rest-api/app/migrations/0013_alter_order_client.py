# Generated by Django 5.0.1 on 2024-03-06 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_client_client_alter_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.client'),
        ),
    ]
