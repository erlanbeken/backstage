from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'backstage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^difference', 'numbers_api.views.difference', name='difference'),
    url(r'^$', 'numbers_api.views.index'),
]
