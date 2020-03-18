from django.urls import path
from . import views

app_name = 'siteapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('sites/', views.sites, name='sites'),
    path('task/', views.task, name='task'),
    path('repository/', views.repository, name='repository'),
    path('taskpage/', views.taskpage, name='taskpage'),
    path('add_site_member/', views.add_site_member, name='add_site_member'),
    path('delete/<str:pk>', views.deleteFile, name='deleteFile'),
    path('deleteSite_Folder/??/=+/<str:pik>/???!!t4/piAss', views.deleteSite_Folder, name='deleteSite_Folder'),
]
