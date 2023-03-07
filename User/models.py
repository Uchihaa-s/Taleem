from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, PermissionsMixin
from django.core.validators import validate_email, FileExtensionValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError


def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('ID contains characters')


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if email is None:
            raise TypeError('Users must have an  email.')
        if password is None:
            raise TypeError('users must have a password.')
        user = self.model(email=self.normalize_email(email))
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')

        user = self.create_user(email, password)
        for x in Group.objects.all():
            x.user_set.add(user)

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Application(models.Model):
    Account_Holder_Name = models.CharField(max_length=500)

    Account_number = models.CharField(max_length=20, validators=[only_int])

    IFSC_Code = models.CharField(max_length=20)

    Resume = models.FileField(validators=[FileExtensionValidator(['pdf'])],blank=True,null=True)

    date_ob_application_submission = models.DateTimeField(auto_now_add=True)

    Status = models.CharField(max_length=20,
        choices=[("Submitted", 'Submitted'), ("Approved", "Approved"), ("Rejected", "Rejected")], default="Submitted")

    Reason = models.TextField()


class User(AbstractBaseUser, PermissionsMixin):
    First_name = models.CharField(max_length=225)

    Last_name = models.CharField(max_length=225)

    Middle_name = models.CharField(max_length=225)

    email = models.EmailField(db_index=True, unique=True, validators=[validate_email], blank=False)

    Reward = models.IntegerField(default=0)

    application=models.ForeignKey(Application,on_delete=models.SET_NULL,null=True,blank=True)

    phone_number = PhoneNumberField(region="IN", null=True, blank=True, )

    is_active = models.BooleanField(default=True)

    is_suspended = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    @property
    def Teacher_approvial(self):
        # todo check status
        return True
