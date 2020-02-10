from django.contrib import admin
from .models import MyUser

# Register your models here.


class MyUserAdmin(admin.ModelAdmin):

    model = MyUser
    list_display = ('user', 'birth_day')
    list_display_links = ('user', )


admin.site.register(MyUser, MyUserAdmin)
