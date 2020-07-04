from .models import *
from django import forms
import django_filters


class MyUserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    firstname = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'search', 'aria-label': 'Search'}))

    class Meta:
        model = MyUser
        fields = ['username', 'firstname', 'surname']


class FolderFilters(django_filters.FilterSet):
    class Meta:
        model = Folder
        fields = ['folder_name', ]
