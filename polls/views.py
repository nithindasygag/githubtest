from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from .models import Peoples
from .serializers import PeoplesSerializer
from .forms import PeopleForm
from rest_framework import viewsets
from rest_framework.response import Response


@csrf_exempt
def index(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        # print(request.POST)
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PeopleForm()
    context = {'form': form}
    return render(request, 'intro.html', context)



@csrf_exempt
def edit(request, id):
    ppl = Peoples.objects.get(pk=id)
    form = PeopleForm(instance=ppl)
    if request.method == 'POST':
        form = PeopleForm(request.POST, instance=ppl)
        if form.is_valid():
            form.save()

    return render(request, 'details.html', {'p': ppl,'form':form})

@csrf_exempt
def list_all(request):
    ppl = Peoples.objects.all()
    return render(request, 'just.html', {'ppl': ppl})

# @csrf_exempt
# def details(request, id):
#     ppl = Peoples.objects.get(pk=id)
#     forms = PeopleForm(request.POST)
#     return render(request, 'list.html', {'ppl': ppl,'forms':forms})


@csrf_exempt
def delete(request, id):
    people = Peoples.objects.get(pk=id)
    people.delete()
    ppl = Peoples.objects.all()
    return render(request, 'just.html', {'ppl': ppl})


class PeoplesViewset(viewsets.ModelViewSet):
    queryset = Peoples.objects.all()
    serializer_class = PeoplesSerializer