from django import forms
from .models import *


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["filepath"]


CHOICES = [('private', 'Private'),
           ('medium', 'Medium'),
           ('public', 'Public')]


class SiteForm(forms.ModelForm):
    site_visibility = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    site_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the name of the site...'}))
    site_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'site id...'}))
    # description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a description for the
    # site...'}))

    class Meta:
        model = Site
        fields = ["site_name", "site_id", "description", 'site_visibility']


class FolderForm(forms.ModelForm):
    folder_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the folder name...'}))

    class Meta:
        model = Folder
        fields = ['folder_name']


class Site_FolderForm(forms.ModelForm):
    folder_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the folder name...'}))

    class Meta:
        model = Site_Folder
        fields = ['folder_name']

# select for dropdown
# choice for radio button
