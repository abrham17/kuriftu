# Generated by Django 5.2 on 2025-04-12 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='resort',
            field=models.ForeignKey(default='hello', on_delete=django.db.models.deletion.CASCADE, related_name='resort_name', to='booking.resorts'),
            preserve_default=False,
        ),
    ]
