from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

admin.site.register(invoice)
admin.site.register(receipt)
admin.site.register(implementation)