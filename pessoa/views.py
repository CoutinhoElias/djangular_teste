from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from pessoa.models import Pessoa, PessoaTelefone, PessoaEndereco
from pessoa.serializers import PessoaSerializer, PessoaTelefoneSerializer, PessoaEnderecoSerializer
from . import serializers

class PessoaList(generics.ListCreateAPIView):
    """
    Lista todos as Pessoas ou cria uma nova pessoa
    """
    queryset = Pessoa.objects.all()
    model = Pessoa
    serializer_class = serializers.PessoaSerializer

class PessoaDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta uma pessoa
    """
    queryset = Pessoa.objects.all()
    model = Pessoa
    serializer_class = serializers.PessoaSerializer

class PessoaTelefoneList(generics.ListCreateAPIView):
    """
    Lista todos os telefones de pessoas ou cria novos telefones de pessoas
    """
    queryset = PessoaTelefone.objects.all()
    model = PessoaTelefone
    serializer_class = serializers.PessoaTelefoneSerializer

class PessoaTelefoneDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta telefones de pessoas
    """
    queryset = PessoaTelefone.objects.all()
    model = PessoaTelefone
    serializer_class = serializers.PessoaTelefoneSerializer

class PessoaEnderecoList(generics.ListCreateAPIView):
    """
    Lista todos as Pessoas ou cria novo Enderecos de pessoas
    """
    queryset = PessoaEndereco.objects.all()
    model = PessoaEndereco
    serializer_class = serializers.PessoaEnderecoSerializer

class PessoaEnderecoDetail(generics.RetrieveUpdateAPIView):
    """
    Busca, atualiza ou deleta Enderecos de pessoas
    """
    queryset = PessoaEndereco.objects.all()
    model = PessoaEndereco
    serializer_class = serializers.PessoaEnderecoSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'pessoa': reverse('pessoa-list', request=request),
        'pessoatelefone': reverse('pessoatelefone-list', request=request),
        'pessoaendereco': reverse('pessoaendereco-list', request=request),
    })