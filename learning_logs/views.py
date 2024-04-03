from django.shortcuts import render
from .models import Topic
from .forms import TopicForms
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """Pagina principal da Aplicação"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    topic = Topic.objects.order_by('date_created')
    context = {'topics':topic}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_created')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    # Classe para adicionar um novo assunto
    if request.method != 'POST':
        # Nada a ser exibido; Será criado um formulario em branco 
        forms = TopicForms()
    else:
        # Dados de POST encontrados. Processsados do POST
        forms = TopicForms(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('check_topics/'))
    
    context = {'form':forms}
    return render(request, 'learning_logs/new_topic.html')
# Create your views here.