# Generated by Django 4.0.2 on 2022-06-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0022_alter_parque_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='estado',
            field=models.CharField(db_column='Estado', default='Disponivel', max_length=255),
        ),
    ]
