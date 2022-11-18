from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            "placeholder": "글 제목을 작성하세요",
        })
    )
    movie_title = forms.CharField(
        label="Movie Title",
        widget=forms.TextInput(attrs={
            "placeholder": "영화 제목을 작성하세요",
        })
    )

    rank = forms.CharField(
        label="Rank",
        widget=forms.TextInput(attrs={
            "placeholder": "영화 점수를 입력하세요",
        })
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            "placeholder": "게시글을 입력하세요",
        })
    )

    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    
    content = forms.CharField(
        label = '댓글',
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