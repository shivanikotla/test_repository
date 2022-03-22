from cgitb import html
from django.contrib import admin
from .models import Interview
# Register your models here.

admin.site.site_header = "Ojas Interview Forms (ADMISTRATION SITE)"
admin.site.site_title = "Ojas Admistration Page"
admin.site.index_title = "Welcome to Interview Evaluation Forms"




# @admin.register(Interview)
# class UserDataAdmin(admin.ModelAdmin):
#     list_display = []

admin.site.register(Interview)
