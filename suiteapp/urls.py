# from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

from django.urls import path
from. import views

app_name = 'suiteapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('mysite/', views.mysite, name='mysite'),
    path('task/', views.task, name='task'),
    path('repository/', views.repository, name='repository'),
    # path('taskpage/', views.taskpage, name='taskpage'),
    path('taskpage/??/<str:name>/', views.taskpageFunc, name='taskpage'),
    path('add_site_member/<str:pk>/', views.add_site_member, name='add_site_member'),
    path('add_site_member_ajax/', views.AjaxHandlerView.as_view(), name='add_site_member_ajax'),
    path('delete_files/<str:dept>/<str:pk>/', views.deleteFile, name='deletefile'),
    # delete_files/<str:dept>/??/+=/<str:pk>/t4/????piAss??/
    path('delete_folder/<str:pk>/??/+=/<str:dep>/t4/????piAss??<str:name>ug/<str:fk>/', views.deleteFolder, name='delete_folder'),
    path('read/<str:pk>/', views.openfile, name='open_file'),
    path('open_department/<str:pk>/', views.openDepartment, name='open_department'),
    path('open_faculty/<str:pk>/', views.openFaculty, name='open_faculty'),
    path('open_folder/<str:pk>/', views.open_folder, name='open_folder'),
    path('formset/', views.formset, name='formset'),
    path('validate_site_name/', views.validate_username, name="validate_site_name"),
    path('save_siteform/', views.save_siteform, name='save_siteform'),
]

