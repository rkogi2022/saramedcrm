from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
class businessProspectsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(business_prospect, businessProspectsAdmin)

class FeedbackAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
admin.site.register(Feedback, FeedbackAdmin)

admin.site.register(conversion_tracker)
