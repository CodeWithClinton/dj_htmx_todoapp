from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def create_todo(request):
    if request.POST.get("task_id"):
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.title = request.POST.get("task")
        task.save()
    else:
        task_name = request.POST.get("task")
        task = Task.objects.create(title=task_name)
        
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'task_list.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    tasks = Task.objects.all()
    task.delete()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)


def change_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed == False:
        task.completed = True
        task.save()
    
    else:
        task.completed = False
        task.save()
        
    
    print(task)
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)

def append_to_form(request, pk):
    task = Task.objects.get(pk=pk)
    print(task.title)
    return HttpResponse(f'''
                        <input type="hidden" value="{task.id}" name="task_id"/>
                        <input id="input" value="{task.title}"placeholder="Enter Todo" name="task" required/>
                        
                        ''')
    
    