from django.contrib import admin
from projects.models import Project, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):		
	list_display = ('name', 'start_date')
	ordering = ('start_date',)
	filter_horizontal = ('tasks',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)