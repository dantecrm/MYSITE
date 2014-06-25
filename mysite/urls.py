from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'polls.views.index'),
    url(r'^detail/$', 'polls.views.detail'),
    url(r'^results/$', 'polls.views.results'),
    url(r'^votar/$', 'polls.views.vote'),
)
