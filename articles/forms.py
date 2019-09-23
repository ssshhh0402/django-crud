from django import forms
from .models import Article, Comment
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=140,
        label='제목',
        help_text='140자 이내로 작성 바랍니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력바랍니다.'
            }
        )
    )    
    class Meta :
        model = Article
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': '제목을 입력바랍니다'
        #         }
        #     )
        # }
        #위젯 설정은 위에 있는 두가지 방법 모두 아무거로나 가능

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        exclude = ('article',)