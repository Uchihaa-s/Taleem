from django.forms import ModelForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView, CreateView

from Questions.modelFormsCustom import AnswerForm, ConversationForm
from Questions.models import Questions, Answer, Conversation
from Reward.models import Reward


class QuestionListView(ListView):
    template_name = "Questions/Question_list.html"
    model = Questions

    def get_queryset(self):
        return super().get_queryset()
    #     queryset = Cats.objects.all()
    #     if self.request.GET.get("browse"):
    #         selection = self.request.GET.get("browse")
    #         if selection == "Cats":
    #             queryset = Cats.objects.all()
    #         elif selection == "Dogs":
    #             queryset = Dogs.objects.all()
    #         elif selection == "Worms":
    #             queryset = Worms.objects.all()
    #         else:
    #             queryset = Cats.objects.all()
    #     return queryset


class QuestionsModelForm(ModelForm):
    class Meta:
        model = Questions
        fields = ["catogery_list",
                  "text",
                  "video",
                  "image",
                  "docs",
                  "user"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                'class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class QuestionsCreationView(CreateView):
    form_class = QuestionsModelForm
    template_name = "Questions/Question_creation_page.html"

    def get_success_url(self):
        return reverse('question_view', kwargs={ 'pk': self.object.id})



class QuestionDetailView(DetailView):
    model = Questions
    template_name = "Questions/Question_Detail.html"


    def get(self, request, *args, **kwargs):
        from django.http import Http404
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['pk']=self.kwargs['pk']
        except Http404:
            # redirect is here
            return redirect(reverse('404_page'))
        # print(Answer.objects.filter(question=self.kwargs['pk']).exists(),
        #       Answer.objects.filter(question=self.kwargs['pk']))
        if Answer.objects.filter(question=self.kwargs['pk']).exists():
            context["Answer"] = Answer.objects.filter(question=self.kwargs['pk'])[0]
            context["Conversation"] = Conversation.objects.filter(question=self.kwargs['pk'])
            context["Reward"] = Reward.objects.filter(question=self.kwargs['pk']).exists()
        else:
            context["Answer"] = False
            context["Answer_form"] = AnswerForm()
        # print(context["object"].video == "")
        return self.render_to_response(context)



class AnswerModelForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question', 'video', 'image',"docs","user"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                'class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class AnswerView(CreateView):
    template_name = "Questions/AnswerView.html"
    form_class = AnswerModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( **kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get(self, request, *args, **kwargs):
        if Answer.objects.filter(question=self.kwargs['pk']).exists():
            return redirect(reverse('404_page'))
        else:
            return super().get(self,request,*args,**kwargs)

    def get_success_url(self):
        return reverse('question_view', kwargs={ 'pk': self.kwargs['pk']})


class ConversationView(CreateView):
    form_class = ConversationForm
    template_name = "Questions/CommentView.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( **kwargs)
        context['pk'] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('question_view', kwargs={ 'pk': self.kwargs['pk']})
