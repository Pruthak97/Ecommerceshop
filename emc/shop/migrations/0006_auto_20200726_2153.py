# Generated by Django 3.0.8 on 2020-07-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200726_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='media/shop/img'),
        ),
    ]
