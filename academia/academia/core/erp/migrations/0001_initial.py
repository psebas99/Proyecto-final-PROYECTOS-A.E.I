# Generated by Django 4.2.8 on 2023-12-22 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150)),
                ('appellidos', models.CharField(max_length=150)),
                ('dpi', models.CharField(max_length=10)),
                ('telefono', models.PositiveIntegerField(default=0)),
                ('name_usuario', models.CharField(max_length=150)),
                ('correo', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
                'ordering': ['id'],
            },
        ),
    ]
