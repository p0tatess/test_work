from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import EducationForm
from .models import EducationModule


def base(request):
    entries = EducationModule.objects.all()

    return render(request,'app_qq/base.html',{'entries':entries})

def show_post(request,post_id):
    num = EducationModule.objects.get(pk=post_id)
    return render(request,'app_qq/show_article.html',{'num':num})

def update(request,post_id):
    try:
        num = EducationModule.objects.get(pk=post_id)
        if request.method == 'POST':
            num.number = request.POST.get('number')
            num.name = request.POST.get('name')
            num.content = request.POST.get('content')
            num.save()
            return HttpResponseRedirect("/")
        else:
            return render(request,'app_qq/update.html',{'num':num})
    except Exception:
        return HttpResponseNotFound("<h2>Этот номер уже занят</h2>")
    # context = {'form':form}
    # return render(request,'app_qq/update.html',context=context)

def delete(request,post_id):
    try:
        num = EducationModule.objects.get(pk=post_id)
        num.delete()
        return HttpResponseRedirect("/")
    except Exception:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def add_article(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()

    else:
        form = EducationForm()

    return render(request,'app_qq/add_module.html',{'form':form})