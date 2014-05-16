from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
)