from django.urls import path

from .views import NewsList, NewsDetail, Search

urlpatterns = [
      path('', NewsList.as_view()),
      path('', Search.as_view()),
      path('<int:pk>', NewsDetail.as_view()),
]