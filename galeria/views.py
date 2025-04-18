from django.shortcuts import render, get_object_or_404

# importar a classe do bd 
from galeria.models import Fotografia

# depois de fazer templates/index.htnl, não precisa mais daqui
# from django.http import HttpResponse

# qnd a requisição for chamada, a pagina será respondida dessa forma 
# chamando os templates
def index(request):
    # return HttpResponse('<h1>Alura Space <h1><h3> by Monique Benevenuto<h3>')
   
    # Não usar mais estrutura de dados, e sim buscar dados da tabela do bd 
    """ dados = {
        1:{"nome": "Nebulosa de Carina", "legenda": "webtelecope.org / NASA / James Webb"},
        2:{"nome": "Galáxia NGC 1079", "legenda": "nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": dados}) """

    # para trazer todos os itens
    # fotografias = Fotografia.objects.all()

    # para trazer só os itens publicados/filtro 
    # fotografias = Fotografia.objects.filter(publicada=True)

    # para ordenar pelo campo data + o campo filtrado (as imagens no site)
    # na ordenação, se quiser decrescente é só colocar o sinal de - na frente do campo
    # fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

""" def imagem(request):
    return render(request, 'galeria/imagem.html') """

# Agora recebendo um parametro foto_id
def imagem(request, foto_id):
    # vai usar um metodo nativo do django para trazer o objeto da foto ou o não encontrado 
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    # verifica se no bd tem fotografia igual ao que esta sendo solicitado no campo buscar do site 
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render (request, "galeria/buscar.html", {"cards": fotografias})