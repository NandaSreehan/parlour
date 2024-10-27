from django.shortcuts import render
from icecream.models import menu

def view(request):
    a=menu.objects.all()
    if request.method=="POST":
        b=request.POST.get('companyname')
        c=request.POST.get('flavor')
        d=request.POST.get('price')
        e=request.POST.get('quantity')
        obj4=menu(brand=b,flavor=c,price=d,quantity=e)
        obj4.save()
        g=menu.objects.all()
        return render(request,'index.html',{'res':g,})
    return render(request,'index.html',{'res':a})
def update(request):
    g=menu.objects.all()
    if request.method=='POST':
        a=int(request.POST.get('idnumber'))
        z=menu.objects.get(id=a)
        b=request.POST.get('brands')
        c=request.POST.get('flavors')
        d=int(request.POST.get('prices'))
        e=int(request.POST.get('quantitys'))
        z.brand=b
        z.flavor=c
        z.price=d
        z.quantity=e
        z.save()
        return render(request,'update.html',{'res':g})
    return render(request,'update.html',{'res':g})
def rem(request):
    g=menu.objects.all()
    if request.method=='POST':
        a=int(request.POST.get('idNumber'))
        z=menu.objects.get(id=a)
        z.delete()
        z.save()
        return render(request,'remove.html',{'res':g})
    return render(request,'remove.html',{'res':g})
    


