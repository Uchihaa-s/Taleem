from django.contrib import admin

# Register your models here.
from Reward.models import Transaction_record, Reward


class Rewardmodeladmin(admin.ModelAdmin):
    list_display = ['question', "date_of_creation","AnswerAccepted"]
    search_fields = ['AnswerAccepted', ]

    class Meta:
        model = Reward



class Transaction_recordmodeladmin(admin.ModelAdmin):
    list_display = ['Account_number', "amount_of_reward_token","user"]
    search_fields = ['Account_number', ]

    class Meta:
        model = Transaction_record

admin.site.register(Reward, Rewardmodeladmin)
admin.site.register(Transaction_record, Transaction_recordmodeladmin)
