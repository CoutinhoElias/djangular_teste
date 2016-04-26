# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nmproduto', models.CharField(max_length=255, verbose_name=b'Nome Produto')),
                ('vlunitarioproduto', models.FloatField(verbose_name=b'Valor Unitario')),
            ],
        ),
    ]
