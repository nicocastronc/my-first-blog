from django.contrib import admin
from .models import Post

admin.site.register(Post) #hacer nuestro modelo visible en la página del administrador.
