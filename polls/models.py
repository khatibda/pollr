# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
    	return self.question_text
    def was_published_recently(self):
	    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	# admin settings #
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
# not in use yet #
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
    	return self.choice_text

# not in use yet #
class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
