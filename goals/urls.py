from django.urls import path
from .views import goal_list, add_goal

urlpatterns = [
    path('list/', goal_list, name='goal_list'),
    path('', goal_list, name='goal_list'),
    path('add/', add_goal, name='add_goal'),
]
