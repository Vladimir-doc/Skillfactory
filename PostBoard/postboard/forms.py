from django import forms
from .models import Ad, Comments





class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['category',
                  'title',
                  'text',
                  ]
        labels = {
            'category': 'Категория',
            'title': 'Заголовок',
            'text': 'Текст',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
