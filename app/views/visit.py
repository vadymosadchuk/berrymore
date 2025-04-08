from django.http import HttpResponseRedirect

from app.models import Visit, User
from .base import CustomCreateView


class VisitCreateView(CustomCreateView):
    model = Visit
    fields = ['client', 'product', 'weight', 'number_of_boxes', 'price_per_kg', 'number_of_boxes_in', 'number_of_boxes_out']
    template_name = 'app/add_object_form.html'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
