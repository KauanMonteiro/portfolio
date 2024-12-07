from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Projeto

def home(request):
    projetos = Projeto.objects.all()
    
    return render(request, 'pages/home.html', context={'projetos': projetos})


def download(request,projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    # Verifica se o arquivo 'executaveis' está presente
    if not projeto.executaveis:
        raise Http404("Arquivo não encontrado")
    
    # Abre o arquivo associado ao campo 'executaveis' e cria a resposta de download
    file_path = projeto.executaveis.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=projeto.executaveis.name.split('/')[-1])
    
    return response
