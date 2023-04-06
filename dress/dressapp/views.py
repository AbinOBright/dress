from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Dress
from . form import DressForm

# Create your views here.
def dress(request):
    iteam=Dress.objects.all()
    context={
        'dress_list':iteam
    }
    return render(request,'iteam.html',context)
def product(request,dress_id):
    dress=Dress.objects.get(id=dress_id)
    return render (request,"detail.html",{'dress':dress})
    # return HttpResponse("this dress no is %s" % dress_id)

def add_dress(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        price = request.POST.get('price',)
        image = request.FILES['img']
        dress = Dress(name=name,desc=desc,price=price,img=image)
        dress.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    dress=Dress.objects.get(id=id)
    form=DressForm(request.POST or None, request.FILES, instance=dress)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'dress':dress})

def delete(request,id):
    if request.method == "POST":
        dress=Dress.objects.get(id=id)
        dress.delete()
        return redirect('/')
    return render(request,'delete.html')
