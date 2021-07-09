from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html


# Create your models here.
# category model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='category/', blank=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    url = models.CharField(max_length=100)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:45px;height:45px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# post model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()
    image = models.ImageField(upload_to='post/', blank=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
