from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from .filters import *
from django.forms import formset_factory, modelformset_factory

# from .functions import handle_uploaded_file
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
@login_required(login_url='login')
def index(request):

    sites = Site.objects.filter(site_visibilty='public' or 'medium')
    siteusers = SiteUser.objects.filter(user=request.user)
    siteform = SiteForm(initial={'created_by':request.user})
    siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user, })
    files = File.objects.all()
    context = {'siteform': siteform, 'sites': sites, 'files': files,
                'siteusers':siteusers, 'siteuserform':siteuserform, }
    return render(request, 'page/index.html', context)


@login_required(login_url='login')
def mysite(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:mysite')

        elif form.is_valid:
            form.save()
            return redirect('suiteapp:mysite')

    else:
        user = request.user
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user, })
        siteform = SiteForm()
        create_folder = FolderForm(initial={'created_by': request.user, 'is_rep': False})
        form = FileForm(initial={'uploaded_by': user})
        folders = Folder.objects.filter(is_rep=False, department=None, faculty=None, created_by=request.user, main_folder=None,)
        files = File.objects.filter(department=None, faculty=None, is_rep=False, folder=None, uploaded_by=request.user) 

        context = {'form': form, 'create_folder': create_folder, 'folders': folders, 'siteuserform':siteuserform,
                   'siteform': siteform, 'files': files}
        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def repository(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('suiteapp:repository')

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:repository')


    else:
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        form = FileForm(initial={'uploaded_by': request.user, 'is_rep': True})
        create_folder = FolderForm(initial={'created_by': request.user})
        siteform = SiteForm(initial={'created_by':request.user})
        files = File.objects.filter(department=None, faculty=None, is_rep=True)
        faculties = Faculty.objects.all()
        departments = Department.objects.all()
        folder_form = FolderForm()
        folders = Folder.objects.filter(is_rep=True, department=None, faculty=None)
        context = {'form': form, 'folder_form': folder_form, 'siteform': siteform, 'faculties':faculties, 'siteuserform':siteuserform,
                   'create_folder': create_folder, 'folders': folders, 'files': files, 'departments':departments, }
        return render(request, 'page/repository.html', context)


@login_required(login_url='login')
def task(request):
    taskform = TaskForm(request.POST, initial={'assigner': request.user})    
    
    if request.method == 'POST':
            
        if taskform.is_valid():
            name = request.POST.get('task_name')
            taskform.save()
            task = Task.objects.get(task_name=name)
            return redirect('suiteapp:taskpage', name)
            
    else:
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        taskform = TaskForm(initial={'assigner': request.user})    
        context = {'siteform': siteform, 'taskform':taskform, 'siteuserform':siteuserform, }
        return render(request, 'page/task.html', context)


@login_required(login_url='login')
def taskpageFunc(request, name):
    TaskDetailformset = modelformset_factory(TaskDetail, fields=('task', 'priority', 'due_date', 'due_time', 'assignee', 'faculty', 
                                                                'department', 'comment', ), extra=5,)
    form = FileForm(request.POST, request.FILES)
    Fileformset = modelformset_factory(File, fields=('filepath', 'task_name'), extra=10)
    
    fileformSet = Fileformset(queryset=(File.objects.filter(task_name=name)), )
    formset = TaskDetailformset(queryset=(TaskDetail.objects.filter(task=name)))
    if request.method == 'POST':
        formset = TaskDetailformset(request.POST, queryset=(TaskDetail.objects.filter(task=name)))
        fileformSet = Fileformset(request.POST, queryset=(File.objects.filter(task_name=name)))
        print(name)
        print(fileformSet.is_valid())
        print(formset.is_valid())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                # instance.pk = sites.site_id
                instance.save()
            return redirect('suiteapp:task')
            

    else:
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        user_list = MyUser.objects.all()
        user_filter = MyUserFilter(request.GET, queryset=user_list)
        form = FileForm(initial={'uploaded_by': request.user, 'is_task': True, })
        context = {'form': form, 'formset': formset, 'siteform':siteform, 'name':name, 'filter':user_filter, 
                   'siteuserform':siteuserform, 'fileformSet':fileformSet,}
        return render(request, 'page/taskpage.html', context)


@login_required(login_url='login')
def add_site_member(request, pk):
    sites = Site.objects.get(site_id=pk)
    SiteUserFormset = modelformset_factory(SiteUser, fields=('site', 'user', 'role',), extra=5,)
    
    if request.method == 'POST':
        formSet = SiteUserFormset(request.POST, queryset=SiteUser.objects.filter(site=sites), min_num=1, validate_min=True)
        print(formSet.is_valid())
        if formSet.is_valid():
            instances = formSet.save(commit=False)
            for instance in instances:
                # instance.pk = sites.site_id
                instance.save()
                
            return redirect('suiteapp:add_site_member', pk)


    siteform = SiteForm(initial={'created_by':request.user})
    siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
    formSet = SiteUserFormset(queryset=SiteUser.objects.filter(site=sites), initial=[{'role':'manager', 'user':request.user}])
    user_list = MyUser.objects.all()
    user_filter = MyUserFilter(request.GET, queryset=user_list)
    context = {'filter': user_filter, 'formset':formSet, 'site':sites,
               'siteform':siteform, 'siteuserform':siteuserform }
    return render(request, 'page/add_site_members.html', context)


@login_required(login_url='login')
def openFolder(request, pk):
    if request.method == 'POST':
        siteuserform = SiteUserForm(request.POST)
        siteform = SiteUser(request.POST,)
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suiteapp:openFolder', pk)

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:openFolder', pk)

    else:
        folders = Folder.objects.get(folder_id=pk)

        create_folder = FolderForm(initial={'is_rep': False, 'created_by': request.user, })
        form = FileForm(initial={'uploaded_by': request.user.id, 'folder': folders})

        files = File.objects.filter(is_rep=False, department=None, faculty=None)
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        open_folder = request.user
        context = {'folders': folders, 'form': form, 'create_folder': create_folder,
                   'open_folder': open_folder, 'siteform':siteform, 'siteuserform':siteuserform,}

        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def openDepartment(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('suiteapp:open_department', pk)

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:open_department', pk)
      

    else:
        files = File.objects.filter(department=request.user.department)
        department = Department.objects.get(dept_id=pk)

        create_folder = FolderForm(
            initial={'is_rep': False, 'created_by': request.user, 'department': request.user.department})

        form = FileForm(initial={'department': request.user.department.dept_id, 'uploaded_by': request.user.id, })

        folders = Folder.objects.filter(is_rep=False, department=request.user.department)
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        context = {'department': department, 'form': form, 'files': files, 'siteform':siteform,
                   'create_folder': create_folder, 'folders': folders, 'siteuserform':siteuserform,}
        return render(request, 'page/open.html', context)


@login_required(login_url='login')
def openFaculty(request, pk):
    if request.method == 'POST':
        siteuserform = SiteUserForm(request.POST)
        siteform = SiteForm(request.POST,)
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)

        if create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:open_faculty', pk)

        elif form.is_valid():
            form.save()
            return redirect('suiteapp:open_faculty', pk)


    else:
        faculty = Faculty.objects.get(faculty_id=pk)
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        create_folder = FolderForm(initial={'is_rep': False, 'faculty': faculty, 'created_by': request.user, })
        form = FileForm(initial={'uploaded_by': request.user, 'faculty': request.user.department.faculty, })
        files = File.objects.filter(is_rep=False, faculty=request.user.department.faculty)
        folders = Folder.objects.filter(is_rep=False, faculty=request.user.department.faculty)
        context = {'faculty': faculty, 'files': files, 'form': form, 'siteform':siteform, 'siteuserform':siteuserform,
                   'create_folder': create_folder, 'folders': folders, }
        return render(request, 'page/open.html', context)


def open_folder(request, pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        create_folder = FolderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('suiteapp:open_folder', pk)

        elif create_folder.is_valid():
            create_folder.save()
            return redirect('suiteapp:open_folder', pk)

    else:
        folders = Folder.objects.get(folder_id=pk)
        siteform = SiteForm(initial={'created_by':request.user})
        siteuserform = SiteUserForm(initial={'role':'manager', 'user':request.user})
        files = File.objects.filter(folder=folders)

        create_folder = FolderForm(initial={'is_rep': False, 'created_by': request.user, 'folder_path': request.path,
                                            'main_folder': folders, })
        form = FileForm(initial={'uploaded_by': request.user.id, 'folder': folders})

        subfolders = Folder.objects.filter(main_folder=folders)

        context = {'form': form, 'create_folder': create_folder, 'siteform':siteform, 'siteuserform':siteuserform,
                   'files': files, 'subfolders': subfolders, }

        return render(request, 'page/open_folder.html', context)


def deleteFolder(request, dep, pk, name, fk):
    folder = Folder.objects.get(folder_id=pk)
    if request.method == 'POST':
        if folder.department == request.user.department:
            folder.delete()
            return redirect('suiteapp:open_department', dep)

        elif folder.faculty == request.user.department.faculty:
            folder.delete()
            return redirect('suiteapp:open_faculty', dep)

        elif folder.main_folder is not None:
            sb = Folder.objects.get(main_folder=fk)
            folder.delete()
            return redirect('suiteapp:open_folder', fk)

        elif folder.department is None and folder.faculty is None and folder.main_folder is None and folder.is_rep is False:
            folder.delete()
            return redirect('suiteapp:mysite')
            
        elif folder.is_rep is True:
            folder.delete()
            return redirect('suiteapp:repository')
    
    context = {'folder': folder, }
    return render(request, 'page/delete.html', context)


@login_required(login_url='login')
def deleteFile(request, dept, pk):
    file = File.objects.get(file_id=pk)
    if request.method == 'POST':

        if file.department == request.user.department:
            file.delete()
            return redirect('suiteapp:open_department', dept)

        elif file.faculty == request.user.department.faculty:
            file.delete()
            return redirect('suiteapp:open_faculty', dept)

        elif file.folder is not None:
            dept = file.folder.folder_id
            file.delete()
            return redirect('suiteapp:open_folder', dept)
        
        elif file.department is None and file.faculty is None and file.folder is None and file.is_rep is False:
            file.delete()
            return redirect('suiteapp:mysite')
            
        elif file.is_rep is True:
            file.delete()
            return redirect('suiteapp:repository')
        
    else:
        context = {'file': file}
        return render(request, 'page/delete.html', context)


@login_required(login_url='login')
def openfile(request, pk):
    file = File.objects.get(file_id=pk)
    return render(request, 'page/doc_page.html', {'file': file})


def search(request):
    user_list = MyUser.objects.all()
    user_filter = MyUserFilter(request.GET, queryset=user_list)
    return render(request, 'page/search.html', {'filter': user_filter})


class AjaxHandlerView(View):
    
    def get(self, request):
        text = request.GET.get('text')
        username = request.GET.get('username')
        user = request.GET.get('user')
        name = request.GET.get('name')
        role = request.GET.get('role')
        ruser = request.GET.get('ruser')
        site = request.GET.get('site')
        context = {'username': username, 'user': user, 'name': name, 'text': text, 
                   'role':role, 'ruser':ruser, 'site':site, }

        if request.is_ajax():

            return JsonResponse(context, status=200)


def formset(request):

    SiteUserFormset = modelformset_factory(SiteUser, fields=('site', 'user', 'role',), extra=5,)
    formSet = SiteUserFormset(queryset=SiteUser.objects.filter(site="teenage-pregnancy"))
    return render(request, 'page/formset.html', {'formset':formSet, })


def validate_username(request):
    username = request.GET.get('site_id')
    print(username)
    data = {'is_taken': Site.objects.filter(site_id=username)}
    print(data)
    return JsonResponse(data)
    

def save_siteform(request):
    site = request.POST.get('site_name')
    
    siteform = SiteForm(request.POST)
    siteuserform = SiteUserForm(request.POST,)

    siteuserform.save()
    siteform.save()
    return redirect('suiteapp:add_site_member', site)

