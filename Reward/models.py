from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


from Questions.models import Questions
from User.models import User

class Reward(models.Model):
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    AnswerAccepted = models.BooleanField(default=False)
    SatisfactionScore = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],default=0)
    date_of_creation = models.DateTimeField(auto_now_add=True)

class Transaction_record(models.Model):
    Account_number=models.CharField(max_length=225)
    image = models.ImageField(upload_to='Transaction_Images_uploaded',null=True,blank=True)
    amount_of_reward_token=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],default=0)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,choices=[("Submitted", 'Submitted'), ("Transacted", "Transacted"), ("declined", "Decline")], default="Submitted")
    date_of_decision = models.DateTimeField(auto_now=True)


