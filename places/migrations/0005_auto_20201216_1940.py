# Generated by Django 3.1.4 on 2020-12-16 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20201216_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='address',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='city',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='places.city'),
        ),
        migrations.AlterField(
            model_name='place',
            name='status',
            field=models.CharField(choices=[('vacant', 'Vacant'), ('occupied', 'Occupied'), ('on_hold', 'On Hold'), ('unknown', 'Unknown')], default='unknown', max_length=8),
        ),
    ]
