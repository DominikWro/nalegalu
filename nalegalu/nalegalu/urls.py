from django.conf.urls import patterns, include, url
from findmovie.views import populate
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^populate$', 'findmovie.views.populate', name='populate'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
