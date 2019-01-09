from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members, name='members'),
    path('members/delete/<int:mem_id>', views.member_delete,
         name='member_delete'),
    path('members/verify/<int:mem_id>', views.member_verify,
         name='member_verify'),
]
