from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('email',)
