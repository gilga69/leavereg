from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name='att'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r"^register/",views.attendancereg,name='att'),
    url(r'^viewall/',views.ulogin,name='all_attendance'),
    url(r'^allleavelist/',views.attview,name='attview'),
]