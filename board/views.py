from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post,Reply
from accounts.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.db.models import Q
# Create your views here.


class PostList(ListView):
    """
    view for rendering all news post if they is approved
    """
    model = Post
    template_name = 'news_list.html'
    queryset = Post.objects.filter(is_approve=True)


class PostDetail(DetailView):
    """
    view for post model instance
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    """
    view for  create post
    """
    model = Post
    template_name = 'post_create.html'
    fields = ('title', 'content', 'category')

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.request.user
        if user.groups.filter(Q(name__in=MyUser.ADMIN) | Q(
                name__in=MyUser.EDITOR)).exists():
            obj.is_approve = True
        else:
            obj.is_approve = False
        myuser = MyUser.objects.get(user=user)
        obj.author = myuser
        return super().form_valid(form)


class ReplyCreate(LoginRequiredMixin, CreateView):
    """
    view for create
    """
    model = Reply
    template_name = 'reply_create.html'
    fields = ('content', )
    pk = ''

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': ReplyCreate.pk})

    def get_context_data(self, **kwargs):
        context = super(ReplyCreate, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        ReplyCreate.pk = self.kwargs['pk']

        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        post = Post.objects.get(id=ReplyCreate.pk)
        obj.post = post
        user = self.request.user
        myuser = MyUser.objects.get(user=user)
        obj.author = myuser
        return super().form_valid(form)
