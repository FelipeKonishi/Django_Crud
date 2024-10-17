from django.urls import path
from .views import lista_produto, cria_produto, edita_produto, deleta_produto

urlpatterns = [
    path('', lista_produto, name='lista_produtos'),
    path('cria/', cria_produto, name='cria_produto'),
    path('edita/<int:pk>/', edita_produto, name='edita_produto'),
    path('deleta/<int:pk>/', deleta_produto, name='deleta_produto'),
]
