from django.db import models

# Create your models here.
class Produto(models.Model):
    nmproduto = models.CharField("Nome Produto", max_length=255)
    vlunitarioproduto = models.FloatField("Valor Unitario")

class ProdutoFornecedor(models.Model):
    """Tabela com os fornecedores dos produtos"""
    nmfornecedor = models.CharField(u'Nome Fornecedor', max_length=100, blank=True)
    produto = models.ForeignKey(Produto, related_name='fornecedores')

    def __unicode__(self):
        return self.nmfornecedor

class ProdutoPreco(models.Model):
    """Tabela com os fornecedores dos produtos"""
    dspreco = models.CharField(u'Nome Preco', max_length=100, blank=True)
    produto = models.ForeignKey(Produto, related_name='precos')

    def __unicode__(self):
        return self.dspreco