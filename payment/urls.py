from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('get_end', views.CreateEndPoint.as_view(), name='create_end'),
	path('validation', csrf_exempt(views.VaidationView.as_view()), name='major'),
	path('confirmation', csrf_exempt(views.ConfirmationView.as_view()), name='major')
]