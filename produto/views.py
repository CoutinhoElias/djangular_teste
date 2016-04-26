from django.shortcuts import render
#PessoaTelefone = ProdutoPreco
#PessoaEndereco = ProdutoFornecedor
# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from produto.models import Produto, ProdutoPreco, ProdutoFornecedor
from produto.serializers import ProdutoSerializer, ProdutoPrecoSerializer, ProdutoFornecedorSerializer
from . import serializers
from django.views.generic import TemplateView

class ProdutoList(generics.ListCreateAPIView):
    """
    Lista todos as Pessoas ou cria uma nova produto
    """
    queryset = Produto.objects.all()
    model = Produto
    serializer_class = serializers.ProdutoSerializer

class ProdutoDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta uma produto
    """
    queryset = Produto.objects.all()
    model = Produto
    serializer_class = serializers.ProdutoSerializer

class ProdutoPrecoList(generics.ListCreateAPIView):
    """
    Lista todos os telefones de pessoas ou cria novos telefones de pessoas
    """
    queryset = ProdutoPreco.objects.all()
    model = ProdutoPreco
    serializer_class = serializers.ProdutoPrecoSerializer

class ProdutoPrecoDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta telefones de pessoas
    """
    queryset = ProdutoPreco.objects.all()
    model = ProdutoPreco
    serializer_class = serializers.ProdutoPrecoSerializer

class ProdutoFornecedorList(generics.ListCreateAPIView):
    """
    Lista todos as Pessoas ou cria novo Enderecos de pessoas
    """
    queryset = ProdutoFornecedor.objects.all()
    model = ProdutoFornecedor
    serializer_class = serializers.ProdutoFornecedorSerializer

class ProdutoFornecedorDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta Enderecos de pessoas
    """
    queryset = ProdutoFornecedor.objects.all()
    model = ProdutoFornecedor
    serializer_class = serializers.ProdutoFornecedorSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'produto': reverse('produto-list', request=request),
        'produtopreco': reverse('produtopreco-list', request=request),
        'produtofornecedor': reverse('produtofornecedor-list', request=request),
    })

class ProdutoView(TemplateView):
    template_name = "produtos_list.html"