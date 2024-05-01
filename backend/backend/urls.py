from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from todo import views

# router=routers.DefaultRouter()
# router.register(r"todos",views.TodoView,"todo")

urlpatterns = [
    # path('',views.index,name="todo"),
    path('admin/', admin.site.urls),
    path('api/',views.todo_list,name="todo_list"),
    # path("api/",include(router.urls))
]
