from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    
    content = forms.CharField(
        label = '댓글 ',
        widget = forms.TextInput(
            attrs = {
                'class' : 'comment-content',
                'row': 2,
                'col': 4,
            }
        )
    )
    class Meta:
        model = Comment
        exclude = ('review', 'user', 'like_users', )