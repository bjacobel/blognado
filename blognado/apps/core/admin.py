from django.contrib import admin
from blognado.apps.core.models import Liveblog, Update

# Some of these we will definitely want to customize later
# But for now the default admin view is fine
admin.site.register(Liveblog)
admin.site.register(Update)