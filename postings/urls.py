from django.urls import path

# from postings.models import Commit
from .views      import PostingView,CommentView,LikeView,FollowView, CountView

urlpatterns = {
  path('posting', PostingView.as_view()),
  path('comment/<int:post_id>', CommentView.as_view()),
  path('like', LikeView.as_view()),
  path('follow', FollowView.as_view()),
  path('count/<int:post_id', CountView.as_view())

  # 127.0.0.1:8000/commit/1
}