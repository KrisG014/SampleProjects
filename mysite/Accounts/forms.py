from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        model = User

        def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args, **kwargs)
            self.fields["email"].label = "Email Address"
            self.fields["first_name"].label = "First Name"
            self.fields["last_name"].label = "Last Name"

