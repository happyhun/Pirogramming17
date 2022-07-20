from django.db import models

# Create your models here.
class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name="이름")
    kind = models.CharField(max_length=50, verbose_name="종류")
    content = models.TextField(verbose_name="컨텐츠")

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="이미지")
    content = models.TextField(verbose_name="컨텐츠")
    interest = models.IntegerField(default=0, verbose_name="관심도")
    devtool = models.ForeignKey(DevTool, on_delete=models.PROTECT)

