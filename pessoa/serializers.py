from rest_framework import serializers
from pessoa.models import Pessoa, PessoaTelefone, PessoaEndereco

class PessoaTelefoneSerializer(serializers.ModelSerializer):
    id = PessoaTelefone.pk
    class Meta:
        model = PessoaTelefone
        fields = ['id', 'tipoTelefone', 'numero', 'descricao']

class PessoaEnderecoSerializer(serializers.ModelSerializer):
    id = PessoaEndereco.pk
    class Meta:
        model = PessoaEndereco
        fields = ['id', 'tipoEndereco', 'logradouro', 'cidade', 'estado', 'endereco', 'bairro', 'cep', 'numero', 'observacao']

class PessoaSerializer(serializers.ModelSerializer):
    telefones = PessoaTelefoneSerializer(many=True)
    enderecos = PessoaEnderecoSerializer(many=True)

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'tipoPessoa', 'documento', 'dataNascimento', 'telefones', 'enderecos']

    def create(self, validated_data):
        telefones_data = validated_data.pop('telefones')
        enderecos_data = validated_data.pop('enderecos')
        pessoa = Pessoa.objects.create(**validated_data)
        nTel = 0
        for telefones in telefones_data:
            PessoaTelefone.objects.create(pessoa=pessoa, **telefones_data[nTel])
            nTel += 1
        nEnd = 0
        for enderecos in enderecos_data:
            PessoaEndereco.objects.create(pessoa=pessoa, **enderecos_data[nEnd])
            nEnd += 1
        return pessoa

    def update(self, instance, validated_data):
        telefones_data = validated_data.pop('telefones')
        enderecos_data = validated_data.pop('enderecos')

        instance.nome = validated_data.get('nome', instance.nome)
        instance.tipoPessoa = validated_data.get('tipoPessoa', instance.tipoPessoa)
        instance.documento = validated_data.get('documento', instance.documento)
        instance.save()

        for fone in telefones_data:
            PessoaTelefone.objects.filter(pk=fone['id']).update(**fone)

        for ende in enderecos_data:
            PessoaEndereco.objects.filter(pk=ende['id']).update(**ende)

        return instance
