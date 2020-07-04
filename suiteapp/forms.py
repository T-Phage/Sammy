from django import forms
from .models import *


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    GEN_CHOICES = [('select', ''),
                   ('male', 'Male'),
                   ('female', 'Female'),
                   ('other', 'Other')]
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'enter password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 're-enter password'}))
    # department = forms.ModelChoiceField(queryset=Department.objects.all(),
    #                                     widget=forms.Select(attrs={'class': 'form-control'}))
    # faculty = forms.ModelChoiceField(queryset=Faculty.objects.all(),
    #                                  widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    othername = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'othernames'}))
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your surname'}))
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter firstname'}))

    # faculty = forms.SelectMultiple(attrs={'required': "required"})

    class Meta:
        model = MyUser
        fields = ('firstname', 'email', 'username', 'department', 'password1',
                  'password2', 'gender', 'surname', 'othername')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["filepath", "uploaded_by", 'department', 'faculty', 'is_rep', 'folder', 'is_task']


CHOICES = [('private', 'Private'),
           ('medium', 'Medium'),
           ('public', 'Public')]


class SiteForm(forms.ModelForm):
    site_visibility = forms.ChoiceField(label='Visibility',choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-ckeck'}))
    site_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter the name of the site...', 'class': 'form-control'}))
    site_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'site id...', 'class': 'form-control', }))
    # description = forms.CharField(widget=forms.TextInput(attrs={'':'form-control'}))

    class Meta:
        model = Site
        fields = ["site_name", "site_id", "description", 'site_visibility', 'created_by',]


class FolderForm(forms.ModelForm):
    folder_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the folder name...'}))

    class Meta:
        model = Folder
        fields = ['folder_name', 'is_rep', 'faculty', 'department', 'created_by', 'main_folder']


class SiteUserForm(forms.ModelForm):
    
    class Meta:
        model = SiteUser
        fields = ['site', 'user', 'role',]


class DateInput(forms.DateInput):
    input_type = 'date'

    def clean_date(self):
        cleaned_data = self.cleaned_data
        due_date = cleaned_data.get("due_date")
        return due_date


class TimeInput(forms.TimeInput):
    input_type = 'time'

    def clean_time(self):
        cleaned_data = self.cleaned_data
        due_time = cleaned_data.get("due_time")
        return due_time


class TimeForm(forms.Form):
    time_field = forms.TimeField(widget=TimeInput())


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', 'assigner', ]


class TaskFileForm(forms.ModelForm):
    # filepath = forms.FileField(
    #     widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control col-sm-4'}))

    class Meta:
        model = File
        fields = ['is_task', 'filepath', 'uploaded_by']
        

# select for dropdown
# choice for radio button
