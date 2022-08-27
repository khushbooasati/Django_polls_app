from django.db import models
import datetime
from django.utils import timezone

# Create your models here.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text




class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    show_date = models.DateTimeField('date published')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True) 
    

    def __str__(self):
        return self.topic_text

    def was_published_recently(self):
        return self.show_date >= timezone.now() - datetime.timedelta(days=1)



class Topic2(models.Model):
    text = models.CharField(max_length=200)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True) 

class Topic3(models.Model):
    text = models.CharField(max_length=200)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    #show_date = models.DateTimeField('date published')     

