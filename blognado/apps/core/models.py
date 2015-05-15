from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Liveblog(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(blank=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Liveblog, self).save(*args, **kwargs)


class Update(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Liveblog)

    content_text = models.TextField()
    content_photo = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)