# Generated by Django 3.1.4 on 2020-12-19 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('authentication', '0002_auto_20201219_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='establishment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='places.establishment'),
            preserve_default=False,
        ),
    ]
