from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.views import View
from django.views.generic import FormView, CreateView
from .forms import UserCreateForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class RegisterView(FormView):
    form_class = UserCreateForm
    success_url = '/'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)