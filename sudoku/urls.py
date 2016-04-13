from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^puzzle/(?P<id>[0-9]+)/$', views.puzzle, name='puzzle'),
]