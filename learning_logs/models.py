from django.db import models

class Topic(models.Model):
    # Um novo assunto a aprender
    text = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        # Devolve a representação e String do modelo
        return self.text
    
class Entry(models.Model):
    # Algo especifico aprendido sobre um assunto
    topic = models.ForeignKey(Topic, on_delete=  models.CASCADE)
    text = models.CharField(max_length = 500)
    date_created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.text[:50]+"..."