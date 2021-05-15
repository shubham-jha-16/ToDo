from django.shortcuts import render, redirect,HttpResponse
from .models import ToDo
# Create your views here.
def home(request):
    todo_list = ToDo.objects.all()
    context = {'app_name': "ToDo App", 'todo_list': todo_list}
    return render(request, 'home.html', context)


def add_todo(request):

    if request.method == 'POST' :
        todo_text = request.POST['todo_text']
        data = ToDo(todo_text=todo_text)
        data.save()
    return redirect('home')

def delete_todo(request, todo_id):
    if request.method == 'POST':
         data = ToDo.objects.get(id=todo_id)
         data.delete()
    return redirect('home')

def edit_todo(request, todo_id):
    data = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo_text = request.POST['edit_text']
        data.todo_text = todo_text
        data.save()
        return redirect('home')


    context = {'app_name': "ToDo App", 'todo_data':data}
    return render(request, 'edit.html', context)