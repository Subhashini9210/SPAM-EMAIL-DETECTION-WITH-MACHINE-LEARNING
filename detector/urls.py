from django.urls import path

from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("service-worker.js", views.service_worker, name="service-worker"),
]
