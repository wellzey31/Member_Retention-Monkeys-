from django.urls import include, path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register", views.register_request, name="register"),
    path('homepage/', views.homepage_view, name='homepage_view'),
]