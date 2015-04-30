from django.conf.urls import include, url, patterns
from django.contrib import admin
from FatBurn import views
from FatBurn.views import Home, StartTheBurn, About, LoginRequired

urlpatterns =  patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^home/', Home.as_view(), name='home'),
    url(r'^startTheBurn/', StartTheBurn.as_view(), name='startTheBurn'),
    url(r'^userDetails/', views.userDetails, name='userDetails'),
    url(r'^loginRequired/', LoginRequired.as_view(), name='loginRequired'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('django_browserid.urls')),
    )
