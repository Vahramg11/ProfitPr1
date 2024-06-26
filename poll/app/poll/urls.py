from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('sign_up/', sign_up, name="sign_up"),
    path('sign_in/', sign_in, name="sign_in"),
    path('add_poll/', add_poll, name='add_poll'),
    path("activate/<int:pk>/", activate),
    path("all_polls/", all_polls, name="all_polls"),
    path("all_active_polls/", get_active_polls, name="all_active_polls"),
    path("all_users/", get_all_users, name="get_all_users"),
    path('log_out/', log_out, name='log_out'),
    path('delete_poll/<int:pk>/', delete_poll, name='delete_poll'),
    path('categories/', get_all_categories, name='get_all_categories'),
    path('polls/<int:poll_id>/vote/<int:option_id>/', vote, name='vote')

]