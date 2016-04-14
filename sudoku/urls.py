from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^puzzle/(?P<id>[0-9]+)/$', views.puzzle, name='puzzle'),
	url(r'^pick/$', views.pick, name='pick'),
	url(r'^filterPuzzles/$', views.filterPuzzles, name='filterPuzzles'),
	url(r'^preview/$', views.preview, name='preview'),
	url('^', include('django.contrib.auth.urls')),

]