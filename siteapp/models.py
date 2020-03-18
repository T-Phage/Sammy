from django.db import models


# Create your models here.
class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file_id) + ":" + str(self.filepath)


class Site(models.Model):
    site_name = models.CharField(max_length=200)
    site_id = models.CharField(max_length=200, primary_key=True)
    description = models.TextField()
    site_visibilty = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    priority = models.CharField(max_length=7)
    deadline = models.DateTimeField()
    assignee = models.CharField(max_length=200)
    comment = models.TextField


class Taskfile(models.Model):
    task_file = models.FileField(upload_to='files/', null=True, verbose_name="")


class Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # created_by =


class Site_Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

