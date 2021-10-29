from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify

class Post(models.Model):
    slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    count_of_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["created_at"]

    def get_api_url(self):
        try:
            return reverse("forum_api:post_detail", kwargs={"slug": self.slug})
        except:
            None

def create_slug(instance, new_slug=None):
    slug = slugify(instance.content)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)