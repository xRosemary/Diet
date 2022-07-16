from django.db import models
from mdeditor.fields import MDTextField
from UserInfo.models import UserInfo

class Category(models.Model):
    type = models.CharField(verbose_name="类型", max_length=20)

    def __str__(self):
        return "%s" % self.type

    class Meta:
        verbose_name_plural="文章类别"

class Article(models.Model):
    title = models.CharField(verbose_name="标题", max_length=40)
    author = models.ForeignKey(UserInfo, verbose_name="作者", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name="分类", on_delete=models.CASCADE)
    desc = models.CharField(verbose_name="摘要", max_length=1024)
    date = models.DateField(verbose_name="发布日期", auto_now=True)
    content = MDTextField()  # 正文
    
    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name_plural='文章信息'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)