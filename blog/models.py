from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import ReadNum
from read_statistics.models import ReadNumExpandMethod


class BlogType(models.Model):  # 博客类型
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['-type_name']


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        ordering = ['-create_time']



