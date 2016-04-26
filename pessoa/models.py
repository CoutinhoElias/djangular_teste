# _*_  encoding: utf-8 _*_
from django.db import models

# Create your models here.

#from .lists import TIPOPESSOA_CB, TIPOFONE_CB, TIPOENDERECO_CB, LOGRADOUROS_CB, UF_CB

TIPOPESSOA_CB = (
    ('F', 'Fisica'),
    ('J', 'Juridica'),
)

TIPOFONE_CB = (
    ('Fix', 'Fixo'),
    ('Cel', 'Celular'),
)

TIPOENDERECO_CB = (
    ('res', 'Residencial'),
    ('cob', 'Cobranca'),
)

LOGRADOUROS_CB = (
    ('rua', 'Rua'),
    ('ave', 'Avenida'),
)

UF_CB = (
    ('CE', 'Ceara'),
    ('SP', 'Sao Paulo'),
    ('--', 'Escolha uma UF'),
)

class Pessoa(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    tipoPessoa = models.CharField(u'Tipo Pessoa', choices=TIPOPESSOA_CB, default='F', max_length=1)
    documento = models.CharField(u'Documento', max_length=14)
    dataNascimento = models.DateField(u'Data Nascimento', blank=True, null=True)
    email = models.EmailField(u'E-mail', max_length=100, blank=True)
    dataCadastro = models.DateTimeField(u'Data Cadastro', auto_now_add=True, editable=False)
    lastChange = models.DateTimeField(u'Última Alteração', auto_now=True)

    class Meta:
        ordering = ('dataCadastro',)

    def __unicode__(self):
        return self.nome


class PessoaTelefone(models.Model):
    """Tabela com os telefones de pessoas"""
    tipoTelefone = models.CharField(u'Tipo Telefone', choices=TIPOFONE_CB, default='fix', max_length=3)
    numero = models.CharField(u'Telefone', max_length=25)
    descricao = models.CharField(u'Descrição', max_length=100, blank=True)
    lastChange = models.DateTimeField(u'Última Alteração', auto_now=True)
    pessoa = models.ForeignKey(Pessoa, related_name='telefones')

    def __unicode__(self):
        return self.numero


class PessoaEndereco(models.Model):
    """Tabela com os Endereços de pessoas"""
    tipoEndereco = models.CharField(u'Tipo Endereço', choices=TIPOENDERECO_CB, default='res', max_length=3)
    logradouro = models.CharField(u'Logradouro', choices=LOGRADOUROS_CB, default='rua', max_length=3)
    cidade = models.CharField(u'Cidade', max_length=60, blank=True)
    estado = models.CharField(u'Estado', choices=UF_CB, default='--', max_length=2)
    endereco = models.CharField(u'Endereço', max_length=100, blank=True)
    bairro = models.CharField(u'Bairro', max_length=50, blank=True)
    cep = models.CharField(u'CEP', max_length=10, blank=True)
    numero = models.CharField(u'Numero', max_length=10, blank=True)
    observacao = models.CharField(u'Observação', max_length=100, blank=True)
    lastChange = models.DateTimeField(u'Última Alteração', auto_now=True)
    pessoa = models.ForeignKey(Pessoa, related_name='enderecos')

    def __unicode__(self):
        return self.endereco