from django.contrib import admin
from models import SetingsRSS
 
 
class SetingsRSSAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
 
admin.site.register(SetingsRSS, SetingsRSSAdmin)
