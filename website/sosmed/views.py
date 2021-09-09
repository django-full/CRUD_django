from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
# Create your views here.



def update(request,update_id):
   obj = get_object_or_404(models.Instagram,id=update_id) ##TUTORIAL TERBARU
   form = forms.Igforms(request.POST or None,instance=obj)
   if request.method == 'POST':
       if form.is_valid():
           form.save()

       return redirect('list')

   context = {
       'forms':form
   }
   return render(request, 'create.html', context)


def delete(request,delete_id):
    models.Instagram.objects.filter(id=delete_id).delete()
    return redirect('list')




def list(request):
    model = models.Instagram.objects.all()
    context ={
        'models':model
    }
    return render(request,'list.html',context)


def create(request):
    form = forms.Igforms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('list')
    context={
    'forms': form
    }

    return render(request,'create.html',context)
