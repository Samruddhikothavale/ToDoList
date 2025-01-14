from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home.models import Task


# Create your views here.
def home(request):
     context = { 'success': False}
     if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        # print(title, desc)
        ins=Task(taskTitle=title , taskdesc=desc)
        ins.save()
        context = { 'success': True}
     return render(request , 'index.html',context)

def task(request):
    allTasks = Task.objects.all()
    context = {'tasks' : allTasks}
   #  print(allTasks)
    for item in allTasks:
      #   print(item.taskTitle)
      print(item.taskdesc)
    return render(request , 'task.html', context)