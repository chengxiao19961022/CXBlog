#coding:utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')

# 博客文章
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # title： 这个字段对应帖子的标题。它是CharField，在SQL数据库中会被转化成VARCHAR。
    # slug：这个字段将会在URLs中使用。slug就是一个短标签，该标签只包含字母，数字，下划线或连接线。我们将通过使用slug字段给我们的blog帖子构建漂亮的，友好的URLs。我们给该字段添加了unique_for_date参数，这样我们就可以使用日期和帖子的slug来为所有帖子构建URLs。在相同的日期中Django会阻止多篇帖子拥有相同的slug。
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    # author：这是一个ForeignKey。这个字段定义了一个多对一（many-to-one）的关系。关联上了user
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    # body：这是帖子的主体。它是TextField，在SQL数据库中被转化成TEXT。
    body = models.TextField()
    # publish：这个日期表明帖子什么时间发布。我们使用Djnago的timezone的now方法来设定默认值。This is just a timezone-aware datetime.now（译者注：这句该咋翻译好呢）。
    publish = models.DateTimeField(default=timezone.now)
    # created：这个日期表明帖子什么时间创建。因为我们在这儿使用了auto_now_add，当一个对象被创建的时候这个字段会自动保存当前日期。
    created = models.DateTimeField(auto_now_add=True)
    # updated：这个日期表明帖子什么时候更新。因为我们在这儿使用了auto_now，当我们更新保存一个对象的时候这个字段将会自动更新到当前日期。
    updated = models.DateTimeField(auto_now=True)
    # 帖子状态
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    # 添加标签
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)  # 根据publish字段进行降序排列过的结果

    # str()方法是当前对象默认的可读表现。Django将会在很多地方用到它例如管理站点中
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CXBlog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])


# 用户评论
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)










