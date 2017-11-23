from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^login/$',
        views.LoginView.as_view(),
        name="login"
    ),
    url(
        r'^register/$',
        views.UserRegistrationView.as_view(),
        name="register"
    ),
    url(
        r'^reset-password/$',
        view=views.PasswordResetView.as_view(),
        name="reset_password"
    ),
    url(
        r'^reset-password/confirm/$',
        views.PasswordResetConfirmView.as_view(),
        name="reset_password_confirm"
    ),
    url(
        r'^user/profile/$',
        views.UserProfileView.as_view(),
        name="profile"
    ),
]
