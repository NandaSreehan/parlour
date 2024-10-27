from django.shortcuts import render
from contacts.models import clist

def con(request):
    list=clist.objects.all()
    if request.method=='POST':
        a=request.POST.get('idnumber')
        z=clist.objects.get(id=a)
        return render(request,'contacts.html',{'res':list,'a':z})        
    return render(request,'contacts.html',{'res':list})
def add(request):
    list=clist.objects.all()
    if request.method=='POST':
        obj=clist(name=request.POST.get('addName'),number=request.POST.get('addNumber'))
        obj.save()
        return render(request,'cAdd.html',{'res':list})
    return render(request,'cAdd.html',{'res':list})
def update(request):
    list=clist.objects.all()
    if request.method=='POST':
        z=clist.objects.get(id=request.POST.get('id'))
        a=request.POST.get('name')
        b=int(request.POST.get('number'))
        z.name=a
        z.number=b
        z.save()
        return render(request,'cUpdate.html',{'res':list})
    return render(request,'cUpdate.html',{'res':list})
def rem(request):
    list=clist.objects.all()
    if request.method=='POST':
        z=clist.objects.get(id=request.POST.get('delete'))
        z.delete()
        
        return render(request,'cDel.html',{'res':list})
    return render(request,'cDel.html',{'res':list})