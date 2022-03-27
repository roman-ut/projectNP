from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewsDetail

urlpatterns = [
      path('', NewsList.as_view()),
      path('<int:pk>', NewsDetail.as_view()),
]