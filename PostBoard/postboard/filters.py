import django_filters
from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateTimeFilter

from .models import Ad
from django.contrib.auth.models import User
from django.forms import DateTimeInput

class AdFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=User.objects.all(),
        lookup_expr='exact',
        label=('Автор'),
        empty_label='Авторы'
    )

    title = CharFilter(
        lookup_expr='icontains',
        label='Заголовок',
    )


    datecalbefore = DateTimeFilter(field_name="dateCreation", lookup_expr="lt",
                                   label='Дата публикации до:',
                                   widget=DateTimeInput(format="%Y-%m-%dT%H:%M",
                                                        attrs={"type": "datetime-local"}, ), )
    datecalafter = DateTimeFilter(field_name="dateCreation", lookup_expr="gt",
                                  label='Дата публикации после:',
                                  widget=DateTimeInput(format="%Y-%m-%dT%H:%M",
                                                       attrs={"type": "datetime-local"}, ), )


    class Meta:
        model = Ad
        fields = {
            'category': ['exact']
        }


class AdCommentsFilter(FilterSet):
    ad = django_filters.ModelChoiceFilter(
        field_name='ad',
        queryset=None,
        label='',
        empty_label='Заголовок',
    )
