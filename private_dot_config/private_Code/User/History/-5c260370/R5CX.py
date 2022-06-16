from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta {question_id}")


def results(request, question_id):
    response = "Estas viendo el resultado de la pregunra %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta {question_id}")