from django.conf.urls import url

from home.views import *

app_name = 'home'
urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'register/', RegisterView.as_view(), name='register')
]

