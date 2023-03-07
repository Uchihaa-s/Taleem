from django.contrib import admin

from Questions.models import Questions, Answer, Conversation, Catogery


class Questionsmodeladmin(admin.ModelAdmin):
    list_display = ['user', "id"]
    search_fields = ['text', ]

    class Meta:
        model = Questions


admin.site.register(Questions, Questionsmodeladmin)


class Answersmodeladmin(admin.ModelAdmin):
    list_display = ['user', "id"]
    search_fields = ['text', ]

    class Meta:
        model = Answer


admin.site.register(Answer, Answersmodeladmin)




class Conversationmodeladmin(admin.ModelAdmin):
    list_display = ['user', "id"]
    search_fields = ['message', ]

    class Meta:
        model = Conversation


admin.site.register(Conversation, Conversationmodeladmin)


class Catogerymodeladmin(admin.ModelAdmin):
    list_display = ['name', "id"]
    search_fields = ['name', ]

    class Meta:
        model = Catogery


admin.site.register(Catogery, Catogerymodeladmin)
