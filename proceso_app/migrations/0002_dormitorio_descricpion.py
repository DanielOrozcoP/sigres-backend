# Generated by Django 4.2.13 on 2024-11-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitorio',
            name='descricpion',
            field=models.CharField(choices=[('Informatica', 'Dormitorio de informaticos'), ('Electricos', 'Dormitorio de electricos')], default='Informatica', max_length=250),
            preserve_default=False,
        ),
    ]
