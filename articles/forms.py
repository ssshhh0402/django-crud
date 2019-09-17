from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     max_length=1,
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '제목을 입력바랍니다.'
    #         }
    #     )
    # )    
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