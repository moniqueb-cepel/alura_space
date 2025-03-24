from django.urls import path
from galeria.views import index, imagem

# criar uma lista de endpoints da aplicação relacionada a galeria
urlpatterns = [
    path('', index),
    # path('imagem', imagem),
    path('galeria/imagem.html', imagem),
]