from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# importar a função index, para ser chamada qnd a pag for carregada
# from galeria.views import index
# Não precisa mais, porque agora esta na urls.py da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    # inclusão de mais uma path
    # path('', index),
    # fazendo de forma para abrangir mais aplicações dentro de galeria
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
