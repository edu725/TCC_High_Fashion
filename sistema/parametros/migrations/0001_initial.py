# Generated by Django 5.1 on 2024-08-29 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=8)),
                ('retirada', models.DecimalField(decimal_places=2, max_digits=8)),
                ('frete', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comissao', models.DecimalField(decimal_places=2, max_digits=8)),
                ('despesas_financeiras', models.DecimalField(decimal_places=2, max_digits=8)),
                ('despesas_comerciais', models.DecimalField(decimal_places=2, max_digits=8)),
                ('lucro', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
