from app.models import ClientGroup
from .base import CustomCreateView


class ClientGroupCreateView(CustomCreateView):
    model = ClientGroup
    fields = ["name"]
    template_name = 'app/add_object_form.html'
    success_url = '/'
