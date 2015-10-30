from django.db import models
from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True
    )
    startup = models.ManyToManyField(
        Startup,
        related_name='blog_post'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='blog_post'
    )

    def __str__(self):
        return "{}: {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))
