from django.contrib import admin
from .models import CallCategory, CallTag, Call

class CallAdmin(admin.ModelAdmin):
    list_display = ('created', 'customer', 'teammember', 'solved', 'title', )
    list_filter = ['solved', 'teammember', 'tags']
    list_editable = ['solved', 'teammember', ]
    search_fields = ['customer', 'teammember', 'title', ]

admin.site.register(CallCategory)
admin.site.register(CallTag)
admin.site.register(Call, CallAdmin)
