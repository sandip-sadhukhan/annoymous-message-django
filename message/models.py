from django.db import models

class Answer(models.Model):
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.content

class UserLink(models.Model):
    name = models.CharField(max_length=100)
    answers = models.ManyToManyField(Answer)
    
    def __str__(self):
        return self.name
