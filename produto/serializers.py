from rest_framework import serializers
from produto.models import Produto, ProdutoPreco, ProdutoFornecedor

class ProdutoPrecoSerializer(serializers.ModelSerializer):
    id = ProdutoPreco.pk
    class Meta:
        model = ProdutoPreco
        fields = ['id', 'dspreco']

class ProdutoFornecedorSerializer(serializers.ModelSerializer):
    id = ProdutoFornecedor.pk
    class Meta:
        model = ProdutoFornecedor
        fields = ['id', 'nmfornecedor']

class ProdutoSerializer(serializers.ModelSerializer):
    precos = ProdutoPrecoSerializer(many=True)
    fornecedores = ProdutoFornecedorSerializer(many=True)

    class Meta:
        model = Produto
        fields = ['id', 'nmproduto', 'vlunitarioproduto', 'precos', 'fornecedores']

    def create(self, validated_data):
        precos_data = validated_data.pop('precos')
        fornecedores_data = validated_data.pop('fornecedores')
        produto = Produto.objects.create(**validated_data)
        nPrec = 0
        for precos in precos_data:
            ProdutoPreco.objects.create(produto=produto, **precos_data[nPrec])
            nPrec += 1
        nForn = 0
        for fornecedores in fornecedores_data:
            ProdutoFornecedor.objects.create(produto=produto, **fornecedores_data[nForn])
            nForn += 1
        return produto

    def update(self, instance, validated_data):
        precos_data = validated_data.pop('precos')
        fornecedores_data = validated_data.pop('fornecedores')

        instance.nmproduto = validated_data.get('nmproduto', instance.nmproduto)
        instance.save()

        for preco in precos_data:
            ProdutoPreco.objects.filter(pk=preco['id']).update(**preco)

        for forn in fornecedores_data:
            ProdutoFornecedor.objects.filter(pk=forn['id']).update(**forn)

        return instance
