from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission

from app.models import User
from app.forms import UserCreateForm
from app.common import selectable_user_permissions
from .base import CustomCreateView


class UserCreateView(CustomCreateView):
    model = User
    template_name = 'app/add_object_form.html'
    success_url = '/'
    form_class = UserCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form['password'].value())
        self.object.save()

        permission_ids = form['user_permissions'].value()
        permissions = list(Permission.objects.filter(id__in=permission_ids, codename__in=selectable_user_permissions))
        self.object.user_permissions.set(permissions)

        return HttpResponseRedirect(self.get_success_url())
