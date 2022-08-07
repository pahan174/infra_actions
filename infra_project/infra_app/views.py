from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось поправить в клик!')


def second_page(request):
    return HttpResponse('А это вторая страница черт побери!')
