from django.urls import path,reverse_lazy
from account.views import user_register, SignUpView, user_login, profile, ProfileEdit, ContactView
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import TemplateView

urlpatterns = [
    path('sign_up/', user_register, name="sign_up"),
    # path('sign_up/', SignUpView.as_view(), name="sign_up"),
    # path('login/', user_login, name="login"),
    # path('login/', LoginView.as_view(template_name = "pages/login.html"), name="login"),
    path('login/', LoginView.as_view(template_name = "pages/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name = "pages/logout.html"), name="logout"),
    path('contact/', ContactView.as_view(), name="contact_page_view"),
    path('profile/', profile, name="profile"),
    path('profile/edit/', ProfileEdit.as_view(), name="profile_edit"),
    path('password-change/', PasswordChangeView.as_view(template_name="pages/password_change.html"), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="pages/password_change_done.html"), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(template_name="pages/password_reset.html", email_template_name = "pages/password_reset_email.html"), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="pages/password_reset_done.html"), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="pages/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="pages/password_reset_complete.html"), name="password_reset_complete"),
]
