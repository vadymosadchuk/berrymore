from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Permission


class CustomCreateView(UserPassesTestMixin, CreateView):
    def get_success_url(self):
        url = super().get_success_url()
        return url.rstrip('/') + f'/?message={self.model.__name__} created successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = self.model.__name__
        return context

    def test_func(self):
        model_permission = Permission.objects.get(codename=f'add_{self.model.__name__.lower()}',
                                                  content_type__app_label='app')
        return self.request.user.is_superuser or (model_permission in self.request.user.user_permissions.all())
