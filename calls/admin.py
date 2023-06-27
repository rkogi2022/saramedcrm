from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
class supportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(support, supportAdmin)

class courtesyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(courtesy, courtesyAdmin)
admin.site.register(director)

