from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'goal_list.html', {'goals': goals})

def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    else:
        form = GoalForm()
    return render(request, 'add_goal.html', {'form': form})