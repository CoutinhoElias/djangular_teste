# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produtofornecedor_produtopreco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nmproduto',
            field=models.CharField(max_length=255, verbose_name='Nome Produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='vlunitarioproduto',
            field=models.FloatField(verbose_name='Valor Unitario'),
        ),
    ]
