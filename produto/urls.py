from django.conf.urls import patterns, url
from produto import views

urlpatterns = patterns('',

    url(r'^$', 'produto.views.api_root'),

    url(r'^produto/$', views.ProdutoList.as_view(), name='produto-list',  ),

    url(r'^produto/(?P<pk>\d+)/$', views.ProdutoDetail.as_view(), name='produto-detail', ),

    url(r'^produtopreco/$', views.ProdutoPrecoList.as_view(), name='produtopreco-list', ),

    url(r'^produtopreco/(?P<pk>\d+)/$', views.ProdutoPrecoDetail.as_view(), name='produtopreco-detail', ),

    url(r'^produtofornecedor/$', views.ProdutoFornecedorList.as_view(), name='produtofornecedor-list', ),

    url(r'^produtofornecedor/(?P<pk>\d+)/$', views.ProdutoFornecedorDetail.as_view(), name='produtofornecedor-detail', ),
)