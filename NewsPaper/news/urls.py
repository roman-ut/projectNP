from django.urls import path

from .views import NewsList, NewsDetail, Search, NewsCreateView, NewsUpdateView, NewsDeleteView, UserUpdateView,\
                   add_subscribe, CategoryList

urlpatterns = [
      path('', NewsList.as_view()),
      path('search', Search.as_view()),
      path('<int:pk>', NewsDetail.as_view(), name='new'),
      path('add/', NewsCreateView.as_view(), name='news_create'),
      path('add/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
      path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
      path('user/', UserUpdateView.as_view(), name='user_update'),
      path('category/', CategoryList.as_view(), name='category'),
      path('subscribe/<int:pk>', add_subscribe, name='subscribe'),
]
