from django import forms
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.http import  request
from .forms import TaskForm
from .models import task
from django.contrib import messages
from django.core.paginator import Page, Paginator
from django.contrib.auth.decorators import login_required



    
def Ola(request):
    return(HttpResponse('Ola'))
@login_required
def tasklist(request) :

    pesquisa=request.GET.get('pesquisa')
    if pesquisa:
      tasks=task.objects.filter(title__icontains=pesquisa)
      
            


    else:  
        
        tasks_lista= task.objects.all().order_by('-create_at')
        paginator = Paginator(tasks_lista,3)
        page=request.GET.get('page')
        tasks =paginator.get_page(page)

    return render(request,'tasks/list.html ',{'tasks':tasks})
@login_required
def taskview(request ,id):
    Task=get_object_or_404(task ,pk=id)
    
    return render(request,"tasks/task.html",{'task':Task})
@login_required
def yourname(request,name) :
    return render(request,'tasks/yourname.html',{'name':name})  
@login_required
def newTask(request):
    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.done='doing'
            task.save()
            messages.info(request,'tarefa' +"  "+ task.title +"  "+'criada com sucesso')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request,'tasks/addtask.html',{'form':form})    

@login_required
def edittask(request,id) :
    Task= get_object_or_404(task,pk=id)
    form = TaskForm(instance=Task)
    if request.method == 'POST':
        form=TaskForm(request.POST,instance=Task)
        if form.is_valid():
            form.save()
            messages.info(request,'tarefa  '+Task.title +'  editada com sucesso')

            return redirect('/')
       
    else:
        return render(request,'tasks/edittask.html',{'form':form,'task':Task})   
@login_required
def deletetask(request,id) :
    Task= get_object_or_404(task,pk=id)
    Task.delete()

    messages.info(request,'tarefa  '+Task.title + '  deletada com sucesso')
    return redirect('/') 


       
          
  




   



