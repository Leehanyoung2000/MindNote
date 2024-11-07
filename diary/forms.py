from django import forms
from .models import Page # 사용할 모델을 가져옵니다.

class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page # 모델 폼에서 사용할 모델과 필드를 명시합니다.
        fields = ['title', 'content', 'feeling', 'score', 'dt_created']
