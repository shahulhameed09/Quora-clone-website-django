from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, regForm
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    questions = Question.objects.exclude(created_by = request.user).order_by('-created_at')
    return render(request, 'index.html', {'questions': questions})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('/')
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_by = request.user
            answer.question = question
            answer.save()
            return redirect('/')
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'question': question, 'form': form})

def view(request, answer_id):
    questions = Question.objects.get(pk=answer_id)
    
    names = request.user
    
    if request.method == "POST":
        likee = request.POST['like']
        ID = request.POST['ans_id']
        answer = Answer.objects.get(id=ID)  
        
        if likee == "unlike":
            answer.likes.remove(names)
        elif likee == "like":
            answer.likes.add(names)
        answer.save()
    
    
    return render(request, 'view.html', {'questions': questions})

def logouts(request):
    logout(request)
    return redirect('accounts/login/')

@login_required
def my_questions(request):
    questions = Question.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'my_question.html', {'questions': questions})

def regs(request):
    a = regForm(request.POST)
    if a.is_valid():
        a.save()
        return redirect('/accounts/login')
    return render(request, 'reg.html', {'form':a})

def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    return redirect('/my_questions')

def delete_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    answer.delete()
    return redirect('/my_questions')