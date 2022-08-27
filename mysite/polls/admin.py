from django.contrib import admin

from .models import Question
from .models import Topic, Topic2,Topic3
from .models import Choice



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_id', 'choice_text']

@admin.register(Topic2)
class Topic2Admin(admin.ModelAdmin):
    list_display = ['text','question']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_text', 'show_date', 'question']

@admin.register(Topic3)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['text',s'question']         

    

  

