from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from app.models import Client


def view_index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    for client in Client.objects.all():
        client.as_dict()

    clients = list(x.as_dict() for x in Client.objects.all().order_by('name'))

    return render(request, 'app/index.html', locals())
