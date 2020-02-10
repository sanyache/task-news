from django.db import models
from django.utils import timezone
from accounts.models import MyUser
from markdown import markdown
from django.utils.html import mark_safe

# Create your models here.


class News(models.Model):
    """
    abstract class that describe  post's author
    """
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Category(models.Model):
    """
    model for category for posts
    """
    category = models.CharField(max_length=100)

    def __str__(self):
        return  '{}'.format(self.category)


class Post(News):
    """
    model that describe post
    """
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    is_approve = models.BooleanField()

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))

    def __str__(self):
        return '"{}" {}'.format(self.title, self.author)


class Reply(News):
    """
    model for reply for post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return "{}".format(self.author)


