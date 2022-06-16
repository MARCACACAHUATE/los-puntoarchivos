from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)

    except Question.DoesNotExist:
        raise Http404("La pregunta no existe alv")

    return render(request, template_name = 'polls/detail.html', context = {'question': question})


def results(request, question_id):
    response = "Estas viendo el resultado de la pregunra %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta {question_id}")