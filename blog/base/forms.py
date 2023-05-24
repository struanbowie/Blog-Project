from django.forms import ModelForm
from .models import Desk

class DeskForm(ModelForm):
	class Meta:
		model = Desk
		fields = '__all__'