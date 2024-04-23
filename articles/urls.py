from django.urls import path
from articles import views


app_name = 'articles'
urlpatterns = [
    path('', views.ArticleListAPIView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailAPIView.as_view(), name='article_detail'),
    path('<int:article_pk>/comments', views.CommentListAPIView.as_view(), name='Comment_list'),
    path('comments/<int:comment_pk>', views.CommentsDetailAPIView.as_view(), name='Comment_detail'),
]
