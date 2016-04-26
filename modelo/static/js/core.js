 /* produtoApp vai ser encontrado em:

 1 - /modelo/modelo/templates/produtos.html:
 na tag <html ng-app="produtoApp">

 */
//Linha 5 do exemplo
var profileEditApp = angular.module('produtoApp', []);


profileEditApp.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);

/* produtoCtrl vai ser encontrado em:

1 - /modelo/modelo/templates/produtos.html:
na tag <div ng-controller="produtoCtrl">


   produtosUrl vai ser encontrado em:

1 - /modelo/modelo/templates/produtos.html:
na tag abaixo:

<script>
     globals = {
        produtosUrl: '{% url "produto" %}'
     }
</script>

   produto vai ser encontrado em:

1 - modelo/modelo/templates/produtos.html:
na tag acima:
2 - modelo/modelo/settings.py:
no nome das apps.
3 - modelo/modelo/urls.py:
nas urls setando a app.
4 - modelo/produto/urls.py:
nas urls da app produto
5 - modelo/produto/serializers.py:
definindo o import da app produto.
 */
profileEditApp.controller('produtoCtrl', function ($scope, $http) {
    $scope.data = {success: false, teste:"pinzi"};

    function getProduto(){
        $http({method: 'GET', url: globals.produtosUrl}).
            success(function(data, status, headers, config) {
                $scope.data.produto = data;
        })
/*eu fiz*/

       $scope.gridOptions={
            data: "produtos"
       };

    }

    getProduto()

    $scope.removerProduto = function(produto){
        $http({method: 'DELETE', url: globals.produtosUrl + produto.id + "/", data: { id: produto.id }}).
        success(function(data, status, headers, config) {
            var index = $scope.data.produto.indexOf(produto);
            if (index != -1) {
                $scope.data.produto.splice(index, 1);
            }
        }).
        error(function(data, status, headers, config) {

        });
    }

    $scope.updateProduto = function() {
        $http({method: 'POST', url: globals.produtosUrl, data: { nmproduto: $scope.data['nmproduto'], vlunitarioproduto: $scope.data['vlunitarioproduto'] }}).
        success(function(data, status, headers, config) {
            $scope.data['success'] = true;
            getProduto();
        }).
        error(function(data, status, headers, config) {
            $scope.data['success'] = false;
        });
    }
});