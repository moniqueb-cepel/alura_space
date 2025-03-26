from django.shortcuts import render

# depois de fazer templates/index.htnl, não precisa mais daqui
# from django.http import HttpResponse

# qnd a requisição for chamada, a pagina será respondida dessa forma 
# chamando os templates
def index(request):
    # return HttpResponse('<h1>Alura Space <h1><h3> by Monique Benevenuto<h3>')
   
    dados = {
        1:{"nome": "Nebulosa de Carina", "legenda": "webtelecope.org / NASA / James Webb"},
        2:{"nome": "Galáxia NGC 1079", "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
