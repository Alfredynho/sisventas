from django.conf.urls import url
from .views import HomeView

urlpatterns = [
    url(r'^dashboard/$', HomeView.as_view(),name='dashboard'),
]