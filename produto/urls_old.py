from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from produto import views

urlpatterns = patterns('',
    url(r'^produto/$', views.ProdutoList.as_view(), name="produto"),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.ProdutoDetail.as_view(), name="comentarios-detail"),
    url(r'^$', views.ProdutoView.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)