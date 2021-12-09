from django.contrib import admin
from .models  import Lead
# Register your models here.

@admin.register(Lead)
class LeadModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','company_name', 'user']
    


