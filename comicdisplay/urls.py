from django.conf.urls import url
from . import views

app_name = 'displaycomics'
urlpatterns = [
	url(r'^(?P<comic_id>[0-9]*)$', views.comicview, name="comicview")
]