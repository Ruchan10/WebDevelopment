from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    # path('', admin.site.urls),
    path("", views.home, name='homePage'),
    path("review/", views.revie, name='ContactPage'),
    path("ongoing/", views.ongoing, name='ongoingPage'),
    path("login/", views.login_page, name='logIn'),
    path("signup/", views.signup, name='signUp'),
]

