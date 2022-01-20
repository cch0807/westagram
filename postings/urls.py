from django.urls import path

# from postings.models import Commit
from .views      import PostingView,CommitView

urlpatterns = {
  path('posting', PostingView.as_view()),
  path('commit/<int:post_id>', CommitView.as_view()),

  # 127.0.0.1:8000/commit/1
}