from django import forms
from .models import Comment, BlogPost

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Write a comment...',
                'class': 'w-full p-2 border border-gray-300 rounded'
            }),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title, Caption / Content',
                'class': 'w-full p-2 border rounded mb-3'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your caption or story...',
                'class': 'w-full p-2 border rounded mb-3',
                'rows': 4
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'mb-3'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        image = cleaned_data.get('image')

        if not content and not image:
            raise forms.ValidationError("You must provide at least content or an image.")
        return cleaned_data