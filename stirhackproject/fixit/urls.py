from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^index/$', views.index, name='index'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^addIssue/$', views.addIssue, name='addIssue'),
	url(r'^register/$', views.register, name='register'),
]