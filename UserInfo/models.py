from django.db import models

# Create your models here.
class UserInfo(models.Model):
    wx_uid = models.CharField(verbose_name="微信号", max_length=30, unique=True)
    userName = models.CharField(verbose_name="姓名", max_length=30)
    age = models.IntegerField(verbose_name="年龄")

    gender_choice = (
		(0, '女性'),
		(1, '男性'),
	)

    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice, default=1)
    phone_number = models.CharField(verbose_name="电话号码", max_length=20)
    occupation = models.CharField(verbose_name="职业", max_length=30)

    class Meta:
        verbose_name_plural='用户信息'

class HealthRecord(models.Model):
    user = models.OneToOneField(verbose_name="用户信息", to="UserInfo", to_field="id", on_delete=models.CASCADE)

    height = models.IntegerField(verbose_name="身高")
    GI = models.FloatField(verbose_name="血糖指数")
    cholesterol = models.FloatField(verbose_name="胆固醇")
    UA = models.FloatField(verbose_name="尿酸指数")
    BP = models.FloatField(verbose_name="血压")

    illness = models.ForeignKey(verbose_name="疾病名称", to="IllnessMode", to_field="id", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural='健康档案'

class IllnessMode(models.Model):
    name = models.CharField(verbose_name="疾病名称", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='疾病种类'