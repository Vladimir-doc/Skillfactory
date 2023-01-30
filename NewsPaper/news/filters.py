from django_filters import FilterSet, DateTimeFilter, CharFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):


    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок',
    )

    datecal = DateTimeFilter(
        field_name="dateCreation",
        lookup_expr="gt",
        label="Дата публикации после:",
        widget=DateTimeInput(format="%Y-%m-%dT%H:%M",
        attrs={"type": "datetime-local"},),
    )


    class Meta:
        model = Post
        fields = {

           'categoryType': ['exact'],
       }

