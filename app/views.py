from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registrationform(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            T=tfd.save()
            nswo=wfd.save(commit=False)
            nswo.topic_name=T
            nswo.save()
            nsao=afd.save(commit=False)
            nsao.name=nswo
            nsao.save()
            return HttpResponse('registration successfull')
        else:
            return HttpResponse('data is in valid ')
    return render(request,'registrationform.html',d)