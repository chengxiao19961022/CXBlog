#coding:utf-8
from django import template

register = template.Library()

from ..models import Post
from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown2


# 统计写过的数量
@register.simple_tag
def total_posts():
    return Post.published.count()

# 统计最新的一些帖子
@register.inclusion_tag('CXBlog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

# 最多的评论
@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
                total_comments=Count('comments')
            ).order_by('-total_comments')[:count]

# # 添加过滤器
# @register.filter(name='markdown')
# def markdown_format(text):
#     return mark_safe(markdown.markdown(text))
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
@register.filter(is_safe=True, name='markdown')
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown2.markdown(force_text(value),
        extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))

# 页码
@register.filter('list')
def do_list(value):
    return range(1, value+1)

from django.utils.html import format_html
@register.simple_tag
def circle_page(curr_page,loop_page,search):
    offset = abs(curr_page - loop_page)
    if offset < 3:
        if curr_page == loop_page:
            page_ele = '<li><a href="?page=%s" class="page active">%s</a></li>'%(loop_page,loop_page)
        else:
            if search:
                page_ele = '<li><a href="?page=%s&search=%s" class="page">%s</a></li>' % (loop_page, search, loop_page)
            else:
                page_ele = '<li><a href="?page=%s" class="page">%s</a></li>'%(loop_page,loop_page)
        return format_html(page_ele)
    else:
        return ''



