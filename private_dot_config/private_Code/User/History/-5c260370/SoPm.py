from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template_name = 'polls/detail.html', context = {'question': question})


def results(request, question_id):
    response = "Estas viendo el resultado de la pregunra %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta {question_id}")