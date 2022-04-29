from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'email']
        labels = {'first_name': "Name"}