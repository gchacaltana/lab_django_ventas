from django.contrib import admin

from applications.sales.models import Currency

# Agregamos al modelo Currency al django admin
admin.site.register(Currency)