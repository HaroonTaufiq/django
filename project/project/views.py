from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Hello, Home!')

def about(request):
    return HttpResponse('About')