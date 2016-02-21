# ------------- forms.py
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ProfileForm, self).__init__(*args, **kwargs)



# ------------- views.py
from django.views.generic import UpdateView


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/success/'

    def get_form_kwargs(self):
        kwargs = super(ProfileUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
