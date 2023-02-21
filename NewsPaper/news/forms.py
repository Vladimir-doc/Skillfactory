from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Category, Author

class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all(), empty_label=())
    title = forms.CharField(label='Заголовок')
    categoryType = forms.ChoiceField(label='Тип категории', choices=Post.CATEGORY_CHOICES)
    postCategory = forms.ModelMultipleChoiceField(label='Категория', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'categoryType',
            'text',
            "postCategory",
        ]

#    def clean(self):
#        cleaned_data = super().clean()
#        description = cleaned_data.get("description")
#        name = cleaned_data.get("name")

#        if name == description:
#            raise ValidationError(
#                "Описание не должно быть идентично названию."
#            )

#        return cleaned_data