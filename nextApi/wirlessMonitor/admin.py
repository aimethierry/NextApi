from django.contrib import admin
from .models import internetMonitor, vpnApi, vpnFile


admin.site.register(internetMonitor)
admin.site.register(vpnApi)
admin.site.register(vpnFile)