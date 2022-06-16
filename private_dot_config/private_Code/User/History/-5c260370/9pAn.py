from django.http import HttpResponse


def index(request):
    return HttpResponse("que onda pinches puerkas")


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta {question_id}")


def results(request, question_id):
    response = "Estas viendo el resultado de la pregunra %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f"Estas votando en la pregunta {question_id}")