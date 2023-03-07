from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from User.models import User


class Catogery(models.Model):
    name = models.CharField(blank=False, null=False,max_length=20,default="")

    def __str__(self):
        return self.name

class Questions(models.Model):
    catogery_list = models.ManyToManyField(Catogery)
    text = models.TextField(blank=False, null=False,default="")
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = models.ImageField(upload_to='Images_uploaded',blank=True,null=True)
    docs = models.FileField(validators=[FileExtensionValidator(['pdf'])],blank=True,null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False,default="")
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image = models.ImageField(upload_to='Images_uploaded',null=True, blank=True,)
    docs = models.FileField(validators=[FileExtensionValidator(['pdf'])],null=True, blank=True,)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Conversation(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    message = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

