# Generated by Django 3.1.4 on 2020-12-20 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_city_user'),
        ('authentication', '0003_userprofile_establishment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='establishment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.establishment'),
        ),
    ]
