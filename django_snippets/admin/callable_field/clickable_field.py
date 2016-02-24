# ---------------- admin.py
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    readonly_fields = ("profile_url")

    def profile_url(self, instance):
        url = reverse_lazy("profile_detail", kwargs={"pk": instance.pk})
        return "<a href=%s>%s</a>" % (url, url)

    profile_url.short_description = "Profile url"
    profile_url.allow_tags = True