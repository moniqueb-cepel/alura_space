from django.shortcuts import render

# depois de fazer templates/index.htnl, não precisa mais daqui
# from django.http import HttpResponse

# qnd a requisição for chamada, a pagina será respondida dessa forma 
# chamando os templates
def index(request):
    # return HttpResponse('<h1>Alura Space <h1><h3> by Monique Benevenuto<h3>')
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
