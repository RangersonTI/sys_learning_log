from django.shortcuts import render
from .models import Topic

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


# Create your views here.