from django.shortcuts import render,redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel

# Create your views here.
def home(request):
    return render(request, 'show_task.html')

def add_task(request):
    if request.method =='POST':
        Task = TaskForm(request.POST)
        if Task.is_valid():
            Task.save()
            print(Task.cleaned_data)
            return redirect('showTask')
    else:
        Task = TaskForm()
    return render(request, 'add_task.html', {'form':Task})

def show_task(request):
    Task = TaskModel.objects.all()
    print(Task)
    return render(request, 'show_task.html',{'data':Task})

def edit_task(request, id):
    Task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = Task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = Task)
        if form.is_valid():
            form.save()
            return redirect('showTask')
    return render(request, 'add_task.html', {'form':form})

def delete_task(request, id):
    Task = TaskModel.objects.get(pk = id).delete()
    return redirect('showTask')

def is_completed(request, id):
    Task = TaskModel.objects.get(pk = id).delete()
    return redirect('showTask')
