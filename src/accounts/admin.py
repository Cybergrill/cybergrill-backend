from django.contrib import admin

from .models import User


# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "id",
        "name",
        "phone",
        "email",
        "role",
        "is_active",
    )


admin.site.register(User, AccountsAdmin)
