from django import forms
from mainapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "price", "owner",)
# фыафыафыа