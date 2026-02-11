from django.contrib import admin
from .models import jobsAppliedTo, jobSeeker, recruiter
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(jobsAppliedTo, ImportExportModelAdmin)
admin.site.register(jobSeeker, ImportExportModelAdmin)
admin.site.register(recruiter, ImportExportModelAdmin)
