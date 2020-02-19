from django import forms
from django.core import validators


class FormName(forms.Form):
    Name = forms.CharField(max_length=60)
    Email = forms.EmailField(help_text="enter a valid email address")
    Verify_Email = forms.EmailField(label="Enter your Email again:")
    Text = forms.CharField(widget=forms.Textarea, max_length=200, min_length=10)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['Email']
        vEmail = all_clean_data['Verify_Email']

        if email != vEmail:
            raise forms.ValidationError("Emails don't match!")
