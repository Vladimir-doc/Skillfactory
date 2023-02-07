from django.urls import path
from .views import (
   PostList, PostDetail, PostSearchList, PostSearchDetail, PostCreate, PostUpdate, PostDelete
)


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('search/', PostSearchList.as_view()),
   path('<int:pk>', PostSearchDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]