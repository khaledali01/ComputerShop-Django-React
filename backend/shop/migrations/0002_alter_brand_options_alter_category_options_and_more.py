# Generated by Django 4.0 on 2022-02-04 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
    ]