from django.urls import path

from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete, \
    UserPostCommentList, comments_accept, comments_delete

urlpatterns = [
    path('', AdList.as_view(), name='ad'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/update/', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
    path('user_posts_comments/', UserPostCommentList.as_view(), name='user_posts_comments'),
    path('user_posts_comments/accept/<int:pk>', comments_accept, name='comments_accept'),
    path('user_posts_comments/delete/<int:pk>', comments_delete, name='comments_delete'),
]
