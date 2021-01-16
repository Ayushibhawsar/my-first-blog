from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = ModelForm
        fields = ['title']

class PostDeleteForm(PostForm):
    class Meta:
        model = PostForm
        fields = []
