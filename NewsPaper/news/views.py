from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .forms import PostForm
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = '-create_datetime'
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostSearchList(ListView):
    model = Post
    ordering = '-create_datetime'
    template_name = 'news/post_search.html'
    context_object_name = 'post_search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.create_post', )
    model = Post
    template_name = 'news/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        post_type = self.request.GET.get('type')
        post = form.save(commit=False)
        if post_type is not None:
            post.post_type = post_type
        else:
            post.post_type = 'NS'
        return super().form_valid(form)


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', )
    model = Post
    template_name = 'news/post_edit.html'
    form_class = PostForm


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )
    model = Post
    template_name = 'news/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')
