from django.shortcuts import render ,redirect
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# from .forms import TodoForm
from .serializers import TodoSerailizer
from .models import ToDo

@api_view(['GET'])
def todo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    snippets = ToDo.objects.all()
    serializer = TodoSerailizer(snippets, many=True)
    return Response(serializer.data)

# class TodoView(viewsets.ModelViewSet):
#     serializer_class=TodoSerailizer
#     queryset=ToDo.objects.all()





# def index(request):
#     item_list=ToDo.objects.order_by("-date")
#     if request.method =="POST":
#         form=TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo')
    
#     form=TodoForm()
    
#     page={
#         "form":form,
#         "list":item_list,
#         "title":"TODO LIST",
#     }
    
#     return render(request,'todo/index.html',page)

