# ------------- validators.py
from django.core.exceptions import ValidationError


def validate_adult_age(age):
    if age < 18:
        msg = 'Must be older that 18 years'
        raise ValidationError(msg)




# AND THIS
# ------------- models.py
from django.db import models


class AdultProfile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[validate_adult_age])



# OR THIS
# ------------- forms.py
from django import forms


class AdultProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdultProfileForm, self).__init__(*args, **kwargs)
        self.fields["age"].validators.append(validate_adult_age)

    class Meta:
        model = AdultProfile
