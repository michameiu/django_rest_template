from django.contrib import admin


# Register your models here.
from client.models import MyUser, ActivityLog


class AdminClass(admin.ModelAdmin):
    list_display = ["id","dummy",'username','phone','dob','role','reset_code','confirm_code','bio','image','gender','allow_notification']

admin.site.register(MyUser,AdminClass)


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ActivityLog._meta.get_fields() if not f.many_to_many and not f.one_to_many]
admin.site.register(ActivityLog,ActivityLogAdmin)