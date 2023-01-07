from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
urlpatterns += staticfiles_urlpatterns()