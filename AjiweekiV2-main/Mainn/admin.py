from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
admin.site.register(Form)
admin.site.register(Questions)

admin.site.register(UserResponse)
admin.site.register(QuestionChoice)
