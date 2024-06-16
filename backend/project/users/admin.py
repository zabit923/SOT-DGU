from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Presentation, Materials, Documents


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'groups', 'date_joined', 'last_login')


admin.site.register(Presentation)
admin.site.register(Materials)
admin.site.register(Documents)
