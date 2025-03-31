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

    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

""" def imagem(request):
    return render(request, 'galeria/imagem.html') """

# Agora recebendo um parametro foto_id
def imagem(request, foto_id):
    # vai usar um metodo nativo do django para trazer o objeto da foto ou o não encontrado 
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})
