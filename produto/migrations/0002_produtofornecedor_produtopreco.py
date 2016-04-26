# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoFornecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nmfornecedor', models.CharField(max_length=100, verbose_name='Nome Fornecedor', blank=True)),
                ('produto', models.ForeignKey(related_name='fornecedores', to='produto.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoPreco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dspreco', models.CharField(max_length=100, verbose_name='Nome Preco', blank=True)),
                ('produto', models.ForeignKey(related_name='precos', to='produto.Produto')),
            ],
        ),
    ]
