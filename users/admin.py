from django.contrib import admin

from .models import UserProfile, TeamMember, Customer

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type', 'display_name', 'newsletter_agreement', )
    list_filter = ['user_type', 'newsletter_agreement', ]
    list_editable = ['display_name', ]
    search_fields = ['username', 'email', 'display_name', ]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(TeamMember)
admin.site.register(Customer)
