from tkinter.constants import CASCADE

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=56, verbose_name='Тэг')


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # tags = models.ManyToManyField(Tag, related_name='articles')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', null=True, blank=True)
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def save(self, *args, **kwargs):
        if self.is_main:
            # Сбросить is_main для всех других тегов этой статьи
            Scope.objects.filter(article=self.article, is_main=True).update(is_main=False)
        super().save(*args, **kwargs)