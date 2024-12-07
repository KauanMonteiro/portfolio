from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Projeto

def home(request):
    projetos = Projeto.objects.all()
    
    return render(request, 'pages/home.html', context={'projetos': projetos})

# Download for Windows Executable (exe)
def download_exe(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    # Check if the 'exe' file exists
    if not projeto.exe:
        raise Http404("Arquivo não encontrado")
    
    # Open the exe file and prepare the response
    file_path = projeto.exe.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=projeto.exe.name.split('/')[-1])
    
    return response

# Download for Linux file
def download_linux(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    # Check if the 'linux' file exists
    if not projeto.linux:
        raise Http404("Arquivo não encontrado")
    
    # Open the linux file and prepare the response
    file_path = projeto.linux.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=projeto.linux.name.split('/')[-1])
    
    return response

# Download for Android APK
def download_apk(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    # Check if the 'apk' file exists
    if not projeto.apk:
        raise Http404("Arquivo não encontrado")
    
    # Open the apk file and prepare the response
    file_path = projeto.apk.path
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=projeto.apk.name.split('/')[-1])
    
    return response
