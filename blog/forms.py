from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
        'class': 'md-textarea form-control'
    }))

    class Meta:
        model = Comment
        fields = ['content']
