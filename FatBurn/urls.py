from django.conf.urls import include, url, patterns
from django.contrib import admin
from FatBurn.views import Home, StartTheBurn, About, LoginRequired

urlpatterns =  patterns('',
    # Examples:
    # url(r'^$', 'FatBurn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^home/', Home.as_view(), name='home'),
    url(r'^startTheBurn/', StartTheBurn.as_view(), name='startTheBurn'),
    url(r'^loginRequired/', LoginRequired.as_view(), name='loginRequired'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('django_browserid.urls')),
    )
