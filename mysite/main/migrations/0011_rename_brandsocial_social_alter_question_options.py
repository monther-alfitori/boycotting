# Generated by Django 5.0 on 2024-09-27 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BrandSocial',
            new_name='Social',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
    ]
