# Generated by Django 4.0 on 2022-01-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=120)),
                ('nombre', models.EmailField(max_length=200)),
            ],
        ),
    ]
