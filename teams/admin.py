from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Equipo,Estadio,Extra

admin.site.register(Equipo)
admin.site.register(Estadio)
admin.site.register(Extra)
admin.site.register(ContentType)
