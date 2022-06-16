from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_name'

    def get_queryset(self):
        """Regresa las ultimas 5 preguntas publicadas"""
        return Question.objects.order_by('-pub_date')[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name = 'polls/detail.html', context = {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Tienes que seleccionar una opcion'
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))