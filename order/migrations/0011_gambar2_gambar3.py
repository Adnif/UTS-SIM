# Generated by Django 4.0 on 2022-05-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_gambar_gambar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gambar2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='gambar')),
            ],
        ),
        migrations.CreateModel(
            name='Gambar3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='gambar')),
            ],
        ),
    ]