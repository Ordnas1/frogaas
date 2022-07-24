from django.db import models
from django.utils.html import mark_safe


class Frog(models.Model):
    """Frog Model"""
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe("<img src='/assets/media/%s' \
        width='150' height='150' />" % (self.image))
