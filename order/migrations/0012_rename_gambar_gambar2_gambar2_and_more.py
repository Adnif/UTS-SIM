# Generated by Django 4.0 on 2022-05-27 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_gambar2_gambar3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gambar2',
            old_name='gambar',
            new_name='gambar2',
        ),
        migrations.RenameField(
            model_name='gambar3',
            old_name='gambar',
            new_name='gambar3',
        ),
    ]