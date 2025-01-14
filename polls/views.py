from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def fuck(request):
    return HttpResponse("hoping this capstone will not fuck my year..")