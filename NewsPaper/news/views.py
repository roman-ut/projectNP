from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from django.core.paginator import Paginator

from .models import Post, PostCategory
from .filters import NewsFilter
from .forms import NewsForm, AuthorForm


class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetail(DetailView):
    template_name = 'new.html'
    queryset = Post.objects.all()


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm

    def get_object(self, **kwargs):
        return self.request.user


class NewsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'add.html'
    form_class = NewsForm
    permission_required = ('news.add_post', )


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'add.html'
    form_class = NewsForm
    permission_required = ('news.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


