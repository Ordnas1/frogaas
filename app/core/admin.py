from django.contrib import admin

from core.models import Frog


class FrogAdmin(admin.ModelAdmin):
    fields = ['image_tag', 'image']
    readonly_fields = ['image_tag']
    list_display = ('id', 'image_tag')


admin.site.register(Frog, FrogAdmin)
