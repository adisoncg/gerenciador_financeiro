# Generated by Django 4.2.5 on 2023-10-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('alimentacao', 'Alimentação'), ('moradia', 'Moradia'), ('estudo', 'Estudo'), ('saude', 'Saúde'), ('transporte', 'Transporte'), ('vestuario', 'Vestuário'), ('lazer', 'Lazer'), ('outro', 'Outro')], max_length=20),
        ),
    ]