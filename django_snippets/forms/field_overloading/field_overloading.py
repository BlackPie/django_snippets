# ------------------ models.py
from django.db import models


# In order to create contact we need only phone number to call back
class Contact(models.Model):
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)




# ------------------ forms.py
from django import forms


# but if we want update the information, we need to make other fields required
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        
    def __init__(self, *args, **kwargs):
        super(ContactUpdateForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = True
        self.fields['name'].required = True
