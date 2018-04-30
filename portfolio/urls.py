from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.works, name='works'),
    url(r'^projects/(?P<work>[-\w]+)$', views.works, name='works'),
    url(r'^projects/(?P<slug>[-\w]+)$', views.works_detail, name='works-detail'),
]
