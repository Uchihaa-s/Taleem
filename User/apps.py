from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    # def ready(self):
    #     from django.contrib.auth.models import Group, Permission
    #
    #     Group.objects.get_or_create(name='Student')
    #     Group.objects.get_or_create(name='Faculty')

        # group.permissions.set(permissions_list)
