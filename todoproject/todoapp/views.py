from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from . models import Task


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskListview(ListView):
    model=Task
    template_name = 'add.html'
    context_object_name = 'task'


class TaskDetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')





# Create your views here.
def add(request):

    task= Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    return  render(request,'add.html',{'task':task})

# def details(request):
#
#     return render(request,'detail.html')

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=Todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})


