from django.views.generic import ListView, DetailView
from .models import Post
from .filters import NewsFilter


class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


