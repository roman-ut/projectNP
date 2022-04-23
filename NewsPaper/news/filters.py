from django_filters import FilterSet
from .models import Post, Category


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'dateCreation': ['gt'],
            'title': ['icontains'],
            'auth': ['exact'],
        }


