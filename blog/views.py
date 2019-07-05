from django.shortcuts import render, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm

# Create your views here.


class PostDetail(ObjectDetailMixin ,View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class TagDetail(ObjectDetailMixin ,View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
