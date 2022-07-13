
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')



