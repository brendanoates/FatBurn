from django.conf.urls import include, url
from django.contrib import admin
from FatBurn.views import Home, StartTheBurn, About

urlpatterns = [
    # Examples:
    # url(r'^$', 'FatBurn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', Home.as_view(), name='home'),
    url(r'^startTheBurn/', StartTheBurn.as_view(), name='startTheBurn'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
]
