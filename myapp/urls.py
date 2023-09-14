from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('logouts', views.logouts, name='logouts'),
    path('regs', views.regs, name='regs'),
    path('create_question/', views.create_question, name='create_question'),
    path('my_questions/', views.my_questions, name='my_questions'),
    path('answer_question/<int:question_id>/', views.answer_question, name='answer_question'),
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('view/<int:answer_id>/', views.view, name='view'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
]    

