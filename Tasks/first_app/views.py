from django.shortcuts import render,redirect
from first_app.form import TaskForm
from first_app.models import TaskModel

# Create your views here.
def show_task(request):
    task=TaskModel.objects.filter(Is_completed=False)
    return render(request,'show_task.html',{'data':task})

def add_task(request):
    if request.method=='POST':
        task=TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('ShowTasks')
    else:
        task=TaskForm()
    return render(request,'add_task.html',{'form':task})

def edit_task(request,id):
    task=TaskModel.objects.get(pk=id)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('ShowTasks')
    return render(request,'add_task.html',{'form':form})

def delete_task(request,id):
    task=TaskModel.objects.get(pk=id).delete()
    return redirect('ShowTasks')

def complete_task(request,id):
    task=TaskModel.objects.get(pk=id)
    task.Is_completed = True
    task.save()
    return redirect('completed')

def completed(request):
    task=TaskModel.objects.filter(Is_completed=True)
    return render(request,'completed.html',{'data':task})
    