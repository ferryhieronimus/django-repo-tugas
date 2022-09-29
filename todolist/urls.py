from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user 
from todolist.views import logout_user
from todolist.views import create_todo
from todolist.views import delete_todo
from todolist.views import update_status
from todolist.views import show_xml

app_name = 'todolist'

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    path("create-task/", create_todo, name="create_todo"),
    path("logout/", logout_user, name="logout"),    
    path("delete/<int:id>", delete_todo, name="delete_todo"),
    path("update/<int:id>", update_status, name="update_status"),
    path('xml/', show_xml, name='show_xml'),
]