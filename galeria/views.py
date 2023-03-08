from django.shortcuts import render


def index(requst):
    return render(requst, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
