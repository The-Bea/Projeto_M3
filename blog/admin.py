from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'data_criacao', 'publicado')
    

    search_fields = ('titulo', 'conteudo')
    

    list_filter = ('publicado', 'data_criacao')


admin.site.register(Post, PostAdmin)