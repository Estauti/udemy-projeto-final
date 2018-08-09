from django.forms import ModelForm
from .models import Produto

class ProductForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'