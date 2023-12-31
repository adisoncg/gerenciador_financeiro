# Generated by Django 4.2.5 on 2023-10-06 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_categoria_gasto_despesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.CharField(max_length=255)),
                ('data_inicio', models.DateField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='despesa',
            name='data',
        ),
        migrations.AddField(
            model_name='despesa',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='despesa',
            name='data_inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Gasto',
        ),
    ]
