from django.contrib import admin

# importa o modelo/classe 
from galeria.models import Fotografia

# para personalizar o grid de fotografias no site 
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("nome", "legenda", "categoria", "descricao", "foto")

    # por default o link já é no primeiro campo
    # mas se quiser modificar, ou colocar em varios campos, é só configurar
    list_display_links = ("nome", "categoria")

    # para colocar campo de busca
    # lembrar de colocar sempre uma virgula no final, por ser tupla
    search_fields = ("categoria",)

# registra o modelo 
admin.site.register(Fotografia, ListandoFotografias)
