from django.forms import ModelForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from Questions.models import Questions, Answer
from Reward.models import Transaction_record, Reward


class TransactionListView(ListView):
    template_name = "Transaction/transaction_list.html"
    model = Transaction_record

    def get_queryset(self):
        return super().get_queryset()


class Transaction_recordModelForm(ModelForm):
    class Meta:
        model = Transaction_record
        fields = ['amount_of_reward_token']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                'class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'


class TransactionCreateView(CreateView):
    template_name = "Transaction/tranasaction_create_view.html"
    form_class = Transaction_recordModelForm

    def get_queryset(self):
        return super().get_queryset()


class RewardModelForm(ModelForm):
    class Meta:
        model = Reward
        fields = ['AnswerAccepted', "SatisfactionScore", "question"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs[
                'class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'


class RewardCreateView(CreateView):
    template_name = "Transaction/Reward_creation_view.html"
    form_class = RewardModelForm

    def get(self, request, *args, **kwargs):
        if not Questions.objects.filter(id=self.kwargs['pk']).exists():
            return redirect(reverse('404_page'))
        elif Reward.objects.filter(question=self.kwargs['pk']).exists():
            return redirect(reverse('404_page'))
        else:
            return super().get(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('question_view', kwargs={ 'pk': self.kwargs['pk']})

    def form_valid(self, form):
        b=super().form_valid(form)
        a=Answer.objects.filter(question=self.kwargs['pk'])[0]
        print(a)
        if self.object.AnswerAccepted == True:
            a.user.Reward+=50
            a.user.Reward +=50*self.object.SatisfactionScore
            a.user.save()
        return b
