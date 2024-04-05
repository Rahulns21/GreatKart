from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Account

class AccountAdminForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget)

    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(),
        }

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'last_login', 'date_joined', 'is_active')
    readonly_fields = ('password', 'last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    form = AccountAdminForm

admin.site.register(Account, AccountAdmin)