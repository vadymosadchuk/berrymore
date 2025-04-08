from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    template_name = 'app/login.html'
    success_url = ''


class LogoutView(BaseLogoutView):
    next_page = '/'
