from django.urls import path
from first_app.views import show_task,add_task,delete_task,edit_task,complete_task,completed

urlpatterns = [
    path('', show_task,name='ShowTasks'),
    path('add_tasks/', add_task,name='AddTasks'),
    path('edit_task/<int:id>', edit_task,name='edittask'),
    path('delete_task/<int:id>', delete_task,name='deletetask'),
    path('complete_task/<int:id>', complete_task,name='completetask'),
    path('completed_task/', completed,name='completed'),
]
