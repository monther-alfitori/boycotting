# Generated by Django 5.0 on 2024-12-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_product_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=1000, upload_to='images/%y/%m/%d'),
        ),
    ]