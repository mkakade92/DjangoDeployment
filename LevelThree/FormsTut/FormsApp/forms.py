from django import forms
from django.core import validators

class FormName(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    verifyemail=forms.EmailField(label="Verify your Email")
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verifyemail']

        if email!=vmail:
            raise forms.ValidationError("Make sure emails match")
    # botcatcher=forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])
    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if(len(botcatcher)>0):
    #         raise form.ValidationError("Bot found")
    #     return botcatcher
