# Generated by Django 3.1.4 on 2020-12-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20201216_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='email',
            field=models.EmailField(default='N/A', max_length=30),
        ),
    ]