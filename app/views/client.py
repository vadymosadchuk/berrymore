from django.shortcuts import render

from app.models import Client
from .base import CustomCreateView


class ClientCreateView(CustomCreateView):
    model = Client
    fields = ["name", 'phone_number', 'group']
    template_name = 'app/add_object_form.html'
    success_url = '/'


def view_client_details(request, client_id):
    if client := Client.objects.filter(id=client_id).first():
        balance = client.get_balance()
    else:
        error = 'client does not exist'

    return render(request, 'app/client_details.html', locals())
