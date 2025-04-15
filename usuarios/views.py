from django.shortcuts import render

# para usar o formulario do django 
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    # return render(request, "usuarios/login.html")
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    # return render(request, "usuarios/cadastro.html")
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})