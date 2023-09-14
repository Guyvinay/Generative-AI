from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
def goodbye_world(request):
    return HttpResponse("Goodbye, World!")