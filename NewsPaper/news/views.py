from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, FormView
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, PostCategory, Category, User
from .filters import NewsFilter
from .forms import NewsForm, AuthorForm, SubscribeForm
from django.template.loader import render_to_string


class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

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


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post',)


class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'category.html'
    context_object_name = 'category'
    paginate_by = 10


class Subscribe (UpdateView):
    template_name = 'subscribe.html'
    queryset = Category.objects.all()
    success_url = '/news/'


@login_required
def add_subscribe(request, pk):
    a = request.user
    # a.save()
    b = Category.objects.get(id=pk)
    b.subscribers.add(a)
    return redirect('/news/')







