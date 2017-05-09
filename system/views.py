from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Home page of graduation work! Authors: Volodymyr Gorobyuk and Kasianchyk Dmytro</h1>'
                        '<p><a href="/api">Go to API</a></p>'
                        '<p><a href="/admin">Go to the admin page</a></p>')