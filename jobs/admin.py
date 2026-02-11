from django.contrib import admin
from .models import job
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(job, ImportExportModelAdmin)
