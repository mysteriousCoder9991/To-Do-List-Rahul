from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success':False,'name':'Rahul'}
    if request.method== "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        dead=request.POST['dead']
        #print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc,dead=dead)
        ins.save()
        context = {'success':True}
    return render(request,'index.html',context)

def tasks(request):
    allTasks=Task.objects.all()
    context={'tasks':allTasks}
    return render(request,'tasks.html',context)