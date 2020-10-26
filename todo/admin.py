from django.contrib import admin
from .models import Todo


class CreateDate(admin.ModelAdmin):
    readonly_fields = ('createDate',)


admin.site.register(Todo, CreateDate)
