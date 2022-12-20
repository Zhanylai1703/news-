# from django.db import models
# from news.models import News

# # Create your models here.

# class Users(models.Model):
#     name = models.CharField("Имя", max_length=100)
#     password = models.CharField(max_length=100)
    

# class UserFavorite(models.Model):
#     users = models.ForeignKey(Users, on_delete=models)
#     news = models.ManyToManyField(News, )