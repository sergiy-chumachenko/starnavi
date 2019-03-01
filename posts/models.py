from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100,
                             blank=False,
                             null=True,
                             verbose_name='Title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='Slug', unique=True)
    body = models.TextField(max_length=5000,
                            blank=False,
                            null=True,
                            verbose_name='Post Text')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', blank=False, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', blank=False, null=True)

    def __str__(self):
        return f'{self.post} from {self.user}'

    def save(self, *args, **kwargs):
        if Like.objects.filter(user=self.user, post=self.post).exists():
            Like.objects.get(user=self.user, post=self.post).delete()
        else:
            super(Like, self).save(*args, **kwargs)
