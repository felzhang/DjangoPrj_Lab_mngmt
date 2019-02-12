from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^classicalbts/$', views.lab_classicalbts, name='classicalbts'),
    url(r'^classicalbts/(?P<classicalbts_id>\d+)/$', views.lab_classicalbts_detail_form, name="classicalbts_detail_form"),
    url(r'^classicalbts-delete-(?P<classicalbts_id>\d+)/$', views.lab_classicalbts_delete, name="classicalbts_delete"),
    url(r'^classicalbts-add/$', views.lab_classicalbts_add, name="classicalbts_add"),

    url(r'^asik/$', views.lab_asik, name='asik'),
    url(r'^asik/(?P<asik_id>\d+)/$', views.lab_asik_detail_form, name="asik_detail_form"),
    url(r'^asik-delete-(?P<asik_id>\d+)/$',views.lab_asik_delete, name="asik_delete"),
    url(r'^asik-add/$', views.lab_asik_add, name="asik_add"),

    url(r'^abil/$', views.lab_abil, name='abil'),
    url(r'^abil/(?P<abil_id>\d+)/$', views.lab_abil_detail_form, name="abil_detail_form"),
    url(r'^abil-delete-(?P<abil_id>\d+)/$', views.lab_abil_delete, name="abil_delete"),
    url(r'^abil-add/$', views.lab_abil_add, name="abil_add"),

    url(r'^gps/$', views.lab_gps, name='gps'),
    url(r'^gps/(?P<gps_id>\d+)/$', views.lab_gps_detail_form, name="gps_detail_form"),
    url(r'^gps-delete-(?P<gps_id>\d+)/$', views.lab_gps_delete, name="gps_delete"),
    url(r'^gps-add/$', views.lab_gps_add, name="gps_add"),

    url(r'^rru/$', views.lab_rru, name='rru'),
    url(r'^rru/(?P<rru_id>\d+)/$', views.lab_rru_detail_form, name="rru_detail_form"),
    url(r'^rru-delete-(?P<rru_id>\d+)/$', views.lab_rru_delete, name="rru_delete"),
    url(r'^rru-add/$', views.lab_rru_add, name="rru_add"),

    url(r'^amia/$', views.lab_amia, name='amia'),
    url(r'^amia/(?P<amia_id>\d+)/$', views.lab_amia_detail_form, name="amia_detail_form"),
    url(r'^amia-delete-(?P<amia_id>\d+)/$', views.lab_amia_delete, name="amia_delete"),
    url(r'^amia-add/$', views.lab_amia_add, name="amia_add"),

    url(r'^pb/$', views.lab_pb, name='pb'),
    url(r'^pb/(?P<pb_id>\d+)/$', views.lab_pb_detail_form, name="pb_detail_form"),
    url(r'^pb-delete-(?P<pb_id>\d+)/$', views.lab_pb_delete, name="pb_delete"),
    url(r'^pb-add/$', views.lab_pb_add, name="pb_add"),
]

