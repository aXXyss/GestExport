from django.contrib import admin

from .models import LieuReceptionDla, RecepTransSciages

# Register your models here.


class LieuReceptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_lieureceptiondla','lieu_reception')

admin.site.register(LieuReceptionDla, LieuReceptionAdmin)

class RecepTransSciagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_receptranssciages','code_reception','code_trans','date_recep_trans', 'lieu_reception', 'receptionnaire')

admin.site.register(RecepTransSciages, RecepTransSciagesAdmin)