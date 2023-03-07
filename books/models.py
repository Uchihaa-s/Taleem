from django.core.validators import FileExtensionValidator
from django.db import models
from Questions.models import Catogery


class Books_model(models.Model):
    book=models.FileField(validators=[FileExtensionValidator(['pdf'])])
    Tittle=models.CharField(max_length=266)
    catogery=models.ForeignKey(Catogery,on_delete=models.CASCADE,default=0)
