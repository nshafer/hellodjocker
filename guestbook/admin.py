from django.contrib import admin

from guestbook.models import Signature


@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'added')
    date_hierarchy = 'added'
