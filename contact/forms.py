from django import forms
from .models import subscribe_model,userprofile

class subscribeform(forms.ModelForm):
    class Meta:
        model = subscribe_model
        fields=['Email']

class userform(forms.ModelForm):
    class Meta:
        model = userprofile
        fields=['name','email','description']






