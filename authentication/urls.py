from django.urls import path, include

from authentication.views import user_profile, signup, signout

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup, name='signup user'),
    path('signout/', signout, name='signout user'),
]