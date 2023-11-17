from django.contrib import admin
from .models import Task

#override basic shown fields on admin panel
class TaskAdmin(admin.ModelAdmin):
  list_display = ('task', 'is_completed', 'updated_at')
  #add a search field in the admin panel
  search_fields = ('task', )

admin.site.register(Task, TaskAdmin)