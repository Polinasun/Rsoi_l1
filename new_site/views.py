from django.http import HttpResponse

from .models import Car

def new_car(request):

    if request.method == "POST":

        if request.POST.get('model'):
            model = request.POST['model']
            car_=Car.objects.create(model = model)
            car_.save()
            return HttpResponse('OK')
        else:
            return HttpResponse ('Model not found')
    else:
        return HttpResponse ('Please write POST')

def get_car(request):

    if request.method == "GET":
        if request.GET.get('model'):
            #filter_result={}
            model = request.GET['model']
            car_=Car.objects.filter(model = model)
            return HttpResponse(', '.join([p_.model for p_ in car_]))
        else:
            return HttpResponse(', '.join([p_.model for p_ in Car.objects.all()]))
    else:
        return HttpResponse('Please write GET')




# Create your views here.
