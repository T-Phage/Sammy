from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Register your models here.
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'filepath', 'uploaded_at')

    class Meta:
        order_with_respect_to = 'file_id'


class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'site_name', 'created_at')


class FolderAdmin(admin.ModelAdmin):
    list_display = ('folder_id', 'folder_name', 'created_on')


class Site_FolderAdmin(admin.ModelAdmin):
    list_display = ('folder_id', 'folder_name', 'created_on')


admin.site.register(File, FileAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(Site_Folder, Site_FolderAdmin)

