# Generated by Django 4.0.2 on 2022-05-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0017_lugar_parqueid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='parqueid',
        ),
        migrations.AddField(
            model_name='zona',
            name='tipo_de_zona',
            field=models.CharField(blank=True, db_column='Estado', max_length=255, null=True),
        ),
    ]