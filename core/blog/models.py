from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post (models.Model):

    class PostObjects(models.Manager):
        def get_posts(self):
            return super().get_posts().filter(status='published')

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)  # PROTECT is for if someone delete any catories it don't effect on post, it won't allow you to delete category

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta():
        ordering = ('-published',)

    def __str__(self):
        self.title
