from django.urls import path
from galeria.views import index, imagem

# criar uma lista de endpoints da aplicação relacionada a galeria
urlpatterns = [
    # path('', index),
    path('', index, name='index'),
    # path('imagem', imagem),
    path('imagem/', imagem, name='imagem'),
]