from django.contrib import admin

from .models import URLEntry

class URLEntryInLine(admin.StackedInline):
    model = URLEntry

class UserAdmin(admin.ModelAdmin):
    inlines = [URLEntryInLine,]
# Register your models here.

admin.site.register(URLEntry)
