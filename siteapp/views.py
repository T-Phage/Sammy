from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from .functions import handle_uploaded_file
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        siteform = SiteForm(request.POST, request.FILES)
        if siteform.is_valid():
            siteform.save()
            return redirect('siteapp:add_site_member')
    else:
        sites = Site.objects.all()
        siteform = SiteForm()
        files = File.objects.all()
        context = {'siteform': siteform, 'sites': sites, 'files': files}
        return render(request, 'index.html', context)


@login_required(login_url='login')
def sites(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        siteform = SiteForm()
        site_folder_form = Site_FolderForm(request.POST)  # create folder form

        if form.is_valid():
            form.save()
            # handle_uploaded_file(request.FILES['filepath'])
            if form.save:
                return redirect('siteapp:sites')

        elif siteform.is_valid():
            siteform.save()
            return redirect('siteapp:add_site_member')

        elif site_folder_form.is_valid():
            site_folder_form.save()
            return redirect('siteapp:sites')

    else:
        siteform = SiteForm()
        form = FileForm(request.POST, request.FILES)
        files = File.objects.all()  # files from database file table
        site_folder_form = Site_FolderForm()  # create folder form
        site_folders = Site_Folder.objects.all()  # site folder table from database

        context = {'form': form, 'site_folder_form': site_folder_form,
                   'siteform': siteform, 'site_folders': site_folders,
                   'files': files}

        return render(request, "mysite.html", context)


@login_required(login_url='login')
def repository(request):
    siteform = SiteForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        folder_form = FolderForm(request.POST)
        siteform = SiteForm()

        if form.is_valid():
            form.save()
            return redirect('siteapp:repository')

        elif folder_form.is_valid():
            folder_form.save()
            return redirect('siteapp:repository')

        elif siteform.is_valid():
            siteform.save()
            return redirect('add_site_member')

    else:
        form = FileForm(request.POST, request.FILES)
        folder_form = FolderForm()
        folders = Folder.objects.all()

        context = {'form': form, 'folder_form': folder_form,
                   'siteform': siteform, 'folders': folders}

        return render(request, "repository.html", context)


@login_required(login_url='accounts:login')
def task(request):
    siteform = SiteForm(request.POST, request.FILES)
    if request.method == 'POST':
        if siteform.is_valid():
            siteform.save()
            return redirect('add_site_member')
    else:
        return render(request, 'task.html', {'siteform': siteform})


@login_required(login_url='login')
def taskpage(request):
    siteform = SiteForm(request.POST, request.FILES)
    if request.method == 'POST':
        if siteform.is_valid():
            siteform.save()
            return redirect('add_site_member')
    else:
        return render(request, 'taskpage.html', {'siteform': siteform})


def add_site_member(request):
    return render(request, 'add_site_members.html')


def deleteFile(request, pk):
    file = File.objects.get(file_id=pk)
    if request.method == 'POST':
        file.delete()
        return redirect('siteapp:sites')
    context = {'file': file}
    return render(request, 'delete.html', context)


def deleteSite_Folder(request, pik):
    site_folder = Site_Folder.objects.get(folder_id=pik)
    if request.method == 'POST':
        site_folder.delete()
        return redirect('siteapp:sites')
    context = {'site_folder': site_folder}
    return render(request, 'delete.html', context)
