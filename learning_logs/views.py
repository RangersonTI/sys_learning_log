from django.shortcuts import render

def index(request):
    """Pagina principal da Aplicação"""
    return render(request, 'learning_logs/index.html')
# Create your views here.