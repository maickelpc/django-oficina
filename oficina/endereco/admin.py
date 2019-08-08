from django.contrib import admin
from .models import Pais, Estado, Viagem

# Register your models here.
class EstadoAdminInline(admin.TabularInline):
    model = Estado
    extra = 0

class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    inlines = [EstadoAdminInline]
    list_display = ['id','nome']
    list_editable = ['nome']
    ordering = ['nome']

admin.site.register(Pais, PaisAdmin)



class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ['id','nome', 'pais']
    list_display_links = ['id', 'nome', 'pais']

    autocomplete_fields = ['pais']


admin.site.register(Estado, EstadoAdmin)



class ViagemAdmin(admin.ModelAdmin):
    search_fields = ['descricao']
    list_display = ['id','descricao', 'data']
    list_display_links = ['id', 'descricao', 'data']
    list_filter = ['data']
    autocomplete_fields = ['paises']
    # add_form_template = 'addviagem.html'


admin.site.register(Viagem, ViagemAdmin)