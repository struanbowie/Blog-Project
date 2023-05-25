from django.forms import ModelForm
from .models import Desk, Post

class DeskForm(ModelForm):
	class Meta:
		model = Desk
		fields = '__all__'

# class PostForm(ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = '__all__'