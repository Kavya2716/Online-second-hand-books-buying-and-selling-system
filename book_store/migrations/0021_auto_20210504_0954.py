# Generated by Django 3.2 on 2021-05-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0020_auto_20210504_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproduct',
            name='b_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='sellproduct',
            name='f_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='sellproduct',
            name='m_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
