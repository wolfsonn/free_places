# Generated by Django 3.1.4 on 2020-12-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20201216_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]