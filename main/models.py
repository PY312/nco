from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return f'{filename}'


class News(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=1000)
    full_description = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='images')

    def __str__(self):
        return self.news.title
