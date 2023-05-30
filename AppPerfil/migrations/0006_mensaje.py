# Generated by Django 4.1.7 on 2023-05-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPerfil', '0005_alter_avatar_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.EmailField(max_length=254)),
                ('receptor', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]
