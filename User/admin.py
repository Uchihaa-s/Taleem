from django.contrib import admin

# Register your models here.
from User.models import User, Application


class Usermodeladmin(admin.ModelAdmin):
    list_display = ['First_name', 'email', "id"]
    search_fields = ['First_name', "email", 'Last_name', 'email']

    class Meta:
        model = User



class Applicationmodeladmin(admin.ModelAdmin):
    list_display = ['date_ob_application_submission', 'Status']
    search_fields = ["Status"]

    # Todo add a reverser user email
    class Meta:
        model = Application

admin.site.register(Application, Applicationmodeladmin)
admin.site.register(User, Usermodeladmin)