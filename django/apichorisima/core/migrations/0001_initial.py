# Generated by Django 4.2.6 on 2023-10-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
