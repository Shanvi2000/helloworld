from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "email", "role", "department", "phone", "joined_date", "is_active")
  list_filter = ("role", "department", "is_active", "joined_date")
  search_fields = ("firstname", "lastname", "email", "phone")
  readonly_fields = ("created_at",)
  
  fieldsets = (
    ("Personal Information", {
      "fields": ("firstname", "lastname", "email", "phone")
    }),
    ("Job Information", {
      "fields": ("role", "department", "working_hours", "salary", "joined_date")
    }),
    ("Status", {
      "fields": ("is_active", "created_at")
    }),
  )
  
admin.site.register(Member, MemberAdmin)

