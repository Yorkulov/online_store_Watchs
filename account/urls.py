from django.urls import path,reverse_lazy
from account.views import user_register, SignUpView, user_login, profile, ProfileEdit
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView

urlpatterns = [
    path('sign_up/', user_register, name="sign_up"),
    # path('sign_up/', SignUpView.as_view(), name="sign_up"),
    # path('login/', user_login, name="login"),
    # path('login/', LoginView.as_view(template_name = "pages/login.html"), name="login"),
    path('login/', LoginView.as_view(template_name = "pages/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name = "pages/logout.html"), name="logout"),
    path('profile/', profile, name="profile"),
    path('profile/edit', ProfileEdit.as_view(), name="profile_edit"),
]
