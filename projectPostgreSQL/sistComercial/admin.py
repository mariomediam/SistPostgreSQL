from django.contrib import admin

from sistComercial.models import Articulos, Question, Choice

# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# class AriculosAdmin(admin.ModelAdmin):
#     fields = ['seccion', 'nombre', 'precio']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']

class AriculosAdmin(admin.ModelAdmin):
    list_display = ('nombre','seccion', 'precio')
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Datos importantes', {'fields': ['precio', 'seccion']}),
    ]
    list_filter = ['seccion']
    search_fields = ['nombre']

admin.site.register(Articulos, AriculosAdmin) 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice) 
