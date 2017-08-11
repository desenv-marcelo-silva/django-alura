from django.shortcuts import render
from perfis.models import Perfil
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == '1':
        perfil = Perfil('Marcelo Silva', 'mlsilva@gmail.com', '(12) 9 9121-6615', 'PrimaSoft')

    if perfil_id == '2':
        perfil = Perfil('Lucia Lopes', 'lucia@gmail.com', '(12) 9 9722-1515', 'CTA/DPC')

    return render(request, 'perfil.html', {'perfil': perfil})