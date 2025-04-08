from app.models import Payment
from .base import CustomCreateView


class PaymentCreateView(CustomCreateView):
    model = Payment
    fields = ['client', 'amount']
    template_name = 'app/add_object_form.html'
    success_url = '/'
