from django.urls import path
from .views import menuItemView , SingleItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu/',menuItemView.as_view()),
    path('menu-item/<int:pk>',SingleItemView.as_view()),
    path('secret/',views.secret),
    path('api-auth-token/',obtain_auth_token)
]