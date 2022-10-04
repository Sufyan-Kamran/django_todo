from django.contrib import admin
from .models import user, todo, donetask, notice
# Register your models here.
admin.site.register(user)
admin.site.register(todo)
admin.site.register(donetask)
admin.site.register(notice)
