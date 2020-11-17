# Create your views here.
# from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from .models import Post, Tag, Category
import markdown
import re


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
    # return render(request, 'blog/index.html', context={
    #    'title': '我的博客首页',
    #    'welcome': '欢迎访问我的博客首页'
    # })
    # return HttpResponse("欢迎访问我的博客首页")


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    post.increase_views()

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',  # 基础扩展
        'markdown.extensions.codehilite',  # 语法高亮扩展
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),  # 允许自动检测生成目扩展
    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, pk):
    # 记得在开始部分导入 Tag 类
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
