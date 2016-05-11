# coding: utf-8
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from django.db import models

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    image_file = models.ImageField(upload_to='original/%Y/%m/%d')
    filtered_image_file = models.ImageField(upload_to='filtered/%Y/%m/%d')
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', '-pk', )

    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('view_single_photo', kwargs={'photo_id': self.id})
