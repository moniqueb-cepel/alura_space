from django.contrib import admin

# importa o modelo/classe 
from galeria.models import Fotografia

# para personalizar o grid de fotografias no site 
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("publicada", "nome", "categoria")

    # por default o link já é no primeiro campo
    # mas se quiser modificar, ou colocar em varios campos, é só configurar
    list_display_links = ("nome",)

    # campo no formato de Busca
    # lembrar de colocar sempre uma virgula no final, por ser tupla
    search_fields = ("nome",)

    # campo no formato de Filtro
    list_filter = ("categoria",)

    # paginação do grid, 10/pagina (nesse exemplo) 
    list_per_page = 10

    # para colocar o campo publicada como editável no grid *****
    # list_editable = ("publicada",)

# registra o modelo 
admin.site.register(Fotografia, ListandoFotografias)
