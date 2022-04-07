from django.urls import path

from .views import NewsList, NewsDetail, Search, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
      path('', NewsList.as_view()),
      path('search', Search.as_view()),
      path('<int:pk>', NewsDetail.as_view(), name='new'),
      path('add/', NewsCreateView.as_view(), name='news_create'),
      path('add/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
      path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
]