from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name= "عنوان")
    content = models.TextField( verbose_name= "متن")
    published_date = models.DateTimeField( verbose_name= "تاریخ انتشار",auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
         return "/post/%i/" % self.id
