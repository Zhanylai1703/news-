# from django.db import models
# from apps.news.models import News
# from apps.users.models import Users

# # Create your models here.
# class Comments(models.Model):
#     user =  models.ForeignKey(Users, related_name='Post', on_delete=models.CASCADE)
#     text = models.TextField(max_length=255, verbose_name='text')
#     date = models.DateTimeField(auto_now_add=True, verbose_name='date publish')
#     news = models.ForeignKey(News, related_name='Post', on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = 'Коммент'
#         verbose_name_plural = 'Комменты'

#     def __str__(self):
#         return self.text
    

# class Likes(models.Model):
#     user = models.ForeignKey(Users, )
#     likes = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
