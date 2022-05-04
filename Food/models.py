from django.core.validators import MinValueValidator
from django.db import models

class NutType(models.Model):
    typeInfo = models.CharField(verbose_name="类别", max_length=20)

    def __str__(self):
        return str(self.typeInfo)

    class Meta:
        verbose_name_plural='营养种类'

class Nutrition(models.Model):
    age = models.IntegerField(verbose_name="年龄", default=0, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return "%s岁所需营养" % self.age

    class Meta:
        verbose_name_plural='人体所需营养'

class Standard(models.Model):
    TypeInfo =  models.ForeignKey("NutType", verbose_name="类别", on_delete=models.CASCADE)

    EAR = models.FloatField(verbose_name="平均需要量", default=0, validators=[MinValueValidator(0)])
    RNI = models.FloatField(verbose_name="推荐摄入量", default=0, validators=[MinValueValidator(0)])
    AI = models.FloatField(verbose_name="适宜摄入量", default=0, validators=[MinValueValidator(0)])
    AMDR = models.FloatField(verbose_name="宏量元素可接受范围", default=0, validators=[MinValueValidator(0)])
    UL = models.FloatField(verbose_name="可耐受最高摄入量", default=0, validators=[MinValueValidator(0)])

    ageInfo = models.ForeignKey("Nutrition", verbose_name="年龄", on_delete=models.CASCADE)

    # def __str__(self):
    #     return "平均需要量:%s| 推荐摄入量:%s| 适宜摄入量:%s| 宏量元素可接受范围:%s| 可耐受最高摄入量:%s" % (self.EAR, self.RNI, self.AI, self.AMDR, self.UL)
    def __str__(self):
        return "%s岁%s的摄入标准" % (self.ageInfo.age, self.TypeInfo)

    class Meta:
        verbose_name_plural='营养摄入标准'