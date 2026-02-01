from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nombre', 'apellido', 'email', 'mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }