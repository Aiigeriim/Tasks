from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import Profile


# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile
    fields = ['birth_date', 'avatar']


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInLine,)

User = get_user_model()
admin.site.unregister(User)

admin.site.register(User, ProfileAdmin)