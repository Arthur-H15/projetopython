from django import forms
from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.http import  request
from .forms import TaskForm
from .models import task
from django.contrib import messages
import datetime
from django.core.paginator import Page, Paginator
from django.contrib.auth.decorators import login_required



    
def Ola(request):
    return(HttpResponse('Ola'))
@login_required
def tasklist(request) :

    tarefascompltas=task.objects.filter(done='done',update_at__gt=datetime.datetime.now()-datetime.timedelta(days=30),user=request.user).count()
    tarefasfeitas=task.objects.filter(done='done',user=request.user).count()
    tarefasnaofeitas=task.objects.filter(done='doing',user=request.user).count()
    pesquisa=request.GET.get('pesquisa')
    filter=request.GET.get('filter')
    if pesquisa:
      tasks=task.objects.filter(title__icontains=pesquisa,user=request.user)
      
    elif filter:
         tasks=task.objects.filter(done=filter,user=request.user)

      
            


    else:  
        
        tasks_lista= task.objects.all().order_by('-create_at').filter(user=request.user)
        paginator = Paginator(tasks_lista,3)
        page=request.GET.get('page')
        tasks =paginator.get_page(page)

    return render(request,'tasks/list.html ',{'tasks':tasks,'taskcomplet': tarefascompltas,'taskdone':tarefasfeitas,'taskdoing':tarefasnaofeitas})
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
            task.user=request.user
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

@login_required
def trocarStatustask  (request,id) :
    Task=get_object_or_404(task,pk=id) 
    if(Task.done=='doing'):
        Task.done='done'
    else:
        Task.done='doing'

    Task.save()  
    return redirect('/')      


       
          
  




   



