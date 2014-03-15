from django.conf.urls import patterns, include, url
from findmovie.views import populate, home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'findmovie.views.home', name='home'),
    url(r'^populate$', 'findmovie.views.populate', name='populate'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
