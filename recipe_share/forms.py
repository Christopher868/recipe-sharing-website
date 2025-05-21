from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserRecipe
from django.forms.widgets import ClearableFileInput

# Form for logging into a account
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


# Form for registering a new user
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# Form for editing user profile
class ChangeUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Form for creating a new recipe
class CreateRecipe(forms.ModelForm):
    class Meta:
        model = UserRecipe
        fields = ['recipe_name', 'recipe_category', 'recipe_picture', 'recipe_difficulty', 'recipe_ingredients', 'required_equipment', 'instructions']
        labels = {
            'recipe_picture': 'Upload Recipe Picture',
        }
