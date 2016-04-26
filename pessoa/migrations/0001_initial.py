# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('tipoPessoa', models.CharField(default=b'F', max_length=1, verbose_name='Tipo Pessoa', choices=[(b'F', b'Fisica'), (b'J', b'Juridica')])),
                ('documento', models.CharField(max_length=14, verbose_name='Documento')),
                ('dataNascimento', models.DateField(null=True, verbose_name='Data Nascimento', blank=True)),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail', blank=True)),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
                ('lastChange', models.DateTimeField(auto_now=True, verbose_name='\xdaltima Altera\xe7\xe3o')),
            ],
            options={
                'ordering': ('dataCadastro',),
            },
        ),
        migrations.CreateModel(
            name='PessoaEndereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoEndereco', models.CharField(default=b'res', max_length=3, verbose_name='Tipo Endere\xe7o', choices=[(b'res', b'Residencial'), (b'cob', b'Cobranca')])),
                ('logradouro', models.CharField(default=b'rua', max_length=3, verbose_name='Logradouro', choices=[(b'rua', b'Rua'), (b'ave', b'Avenida')])),
                ('cidade', models.CharField(max_length=60, verbose_name='Cidade', blank=True)),
                ('estado', models.CharField(default=b'--', max_length=2, verbose_name='Estado', choices=[(b'CE', b'Ceara'), (b'SP', b'Sao Paulo'), (b'--', b'Escolha uma UF')])),
                ('endereco', models.CharField(max_length=100, verbose_name='Endere\xe7o', blank=True)),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro', blank=True)),
                ('cep', models.CharField(max_length=10, verbose_name='CEP', blank=True)),
                ('numero', models.CharField(max_length=10, verbose_name='Numero', blank=True)),
                ('observacao', models.CharField(max_length=100, verbose_name='Observa\xe7\xe3o', blank=True)),
                ('lastChange', models.DateTimeField(auto_now=True, verbose_name='\xdaltima Altera\xe7\xe3o')),
                ('pessoa', models.ForeignKey(related_name='enderecos', to='pessoa.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaTelefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoTelefone', models.CharField(default=b'fix', max_length=3, verbose_name='Tipo Telefone', choices=[(b'Fix', b'Fixo'), (b'Cel', b'Celular')])),
                ('numero', models.CharField(max_length=25, verbose_name='Telefone')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('lastChange', models.DateTimeField(auto_now=True, verbose_name='\xdaltima Altera\xe7\xe3o')),
                ('pessoa', models.ForeignKey(related_name='telefones', to='pessoa.Pessoa')),
            ],
        ),
    ]
