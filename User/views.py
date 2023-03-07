from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from User.models import Application, User

class ApplicationModelForm(ModelForm):
    class Meta:
        model = Application
        fields = ['Account_Holder_Name', "Account_number","IFSC_Code","Resume"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class ApplicationCreateView(CreateView):
    template_name = "registration/ApplicationCreation.html"
    form_class = ApplicationModelForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.application != None:
            return redirect(reverse('404_page'))
        else:
            return super().get(self,request,*args,**kwargs)

    def form_valid(self, form):

        b=super().form_valid(form)
        self.object.save()
        self.request.user.application=self.object
        self.request.user.save()
        return b

    def get_success_url(self):
        return reverse('profile',)


class SignupModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "First_name",
            "Last_name",
            "Middle_name",
            "email",
            "phone_number",
            "password1",
            "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class SignupCreateView(CreateView):
    template_name = "registration/Signup.html"
    form_class = SignupModelForm
    def get_success_url(self):
        return reverse('profile',)



class ProfileModelForm(ModelForm):
    class Meta:
        model = User
        fields = [
           "First_name",
            "Last_name",
            "Middle_name",
            "email",
            "phone_number","id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class ProfileUpdateView(UpdateView):
    template_name = "registration/UpdateProfile.html"
    form_class = ProfileModelForm

    def get(self, request, *args, **kwargs):
        print(request.user.id == self.kwargs['pk'])
        if not( request.user.is_authenticated and request.user.id == self.kwargs['pk']):
            return redirect(reverse('404_page'))
        else:
            return super().get(self,request,*args,**kwargs)
