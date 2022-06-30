# Generated by Django 4.0.2 on 2022-06-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0026_alter_lugar_numero_do_lugar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parque',
            name='foto',
            field=models.FileField(blank=True, db_column='Foto', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='numero_do_lugar',
            field=models.IntegerField(blank=True, db_column='Numero do lugar', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='zona',
            name='numero_da_zona',
            field=models.IntegerField(blank=True, db_column='Numero da zona', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='zona',
            name='tipo_de_zona',
            field=models.CharField(blank=True, db_column='Tipo de zona', max_length=255, null=True),
        ),
    ]
