from django.contrib import admin

from .models import User, URLEntry

class URLEntryInLine(admin.StackedInline):
    model = URLEntry

class UserAdmin(admin.ModelAdmin):
    inlines = [URLEntryInLine,]
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(URLEntry)
