from django.contrib import admin
from django.urls import path, include

# importar a função index, para ser chamada qnd a pag for carregada
# from galeria.views import index
# Não precisa mais, porque agora esta na urls.py da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    # inclusão de mais uma path
    # path('', index),
    # fazendo de forma para abrangir mais aplicações dentro de galeria
    path('', include('galeria.urls')),
]
