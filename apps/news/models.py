from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=150, blank = True, verbose_name='название')
    photo = models.ImageField(upload_to="media")
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    date_of_upload = models.DateTimeField(auto_now_add=True, verbose_name='date publish')
    news_category = models.ForeignKey('Category',related_name='products', on_delete=models.CASCADE,)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

        
        
    def __str__(self):
        return self.title





