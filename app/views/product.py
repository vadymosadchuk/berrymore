from app.models import Product
from .base import CustomCreateView


class ProductCreateView(CustomCreateView):
    model = Product
    fields = ["name"]
    template_name = 'app/add_object_form.html'
    success_url = '/'
