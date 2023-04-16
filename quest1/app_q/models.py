from django.db import models
from django.urls import reverse


class EducationModule(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=255)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_id':self.pk})

    class Meta:
        ordering = ['number']
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'

    def __str__(self):
        return self.name