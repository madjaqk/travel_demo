from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="travels"),
	url(r'^add_travel$', views.new, name="new_plan"),
	url(r'^show_travel/(?P<id>\d+)$', views.show, name="show_plan"),
	url(r'^join/(?P<id>\d+)$', views.join, name="join"),
	url(r'^create', views.create, name="create_trip"),
]
