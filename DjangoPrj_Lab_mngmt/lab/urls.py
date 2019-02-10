from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classicalbts', views.lab_classicalbts, name="classicalBTS"),
    url(r'^asik/$', views.lab_asik, name='asik'),
    url(r'^asik/(?P<asik_id>\d+)/$', views.lab_asik_detail_form, name="asik_detail_form"),
    url(r'^asik-delete-(?P<asik_id>\d+)/$',views.lab_asik_delete, name="asik_delete"),
    url(r'^asik-add/$', views.lab_asik_add, name="asik_add"),
    url(r'^abil', views.lab_abil, name='abil'),
]