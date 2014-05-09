from django.conf.urls import patterns, include, url
from projects.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects_in_progress/projects/$', projectsInProgress),
    url(r'^projects_in_progress/create_project/$', createProject),
    url(r'^projects_in_progress/add_task/$', addTask),
    url(r'^projects_in_progress/projects/tasks/receipt/$', generateReceipt),
    url(r'^projects_completed/$', projectsCompleted),
    url(r'^projects_in_progress/projects/tasks/$', tasks),
)
