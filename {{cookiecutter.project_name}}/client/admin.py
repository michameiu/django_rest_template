from django.contrib import admin
from models import MyUser
# Register your models here.
class AdminClass(admin.ModelAdmin):
    list_display = ["id",'username','phone','dob','bio','image','gender','allow_notification']

admin.site.register(MyUser,AdminClass)