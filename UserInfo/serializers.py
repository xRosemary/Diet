from rest_framework import serializers
from .models import UserInfo, HealthRecord, IllnessMode

class UserInfoModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label="id", read_only=True)
    wx_uid = serializers.CharField(label="微信号", max_length=30)
    userName = serializers.CharField(label="姓名", max_length=30)
    age = serializers.IntegerField(label="年龄")

    gender_choice = (
		(0, '女性'),
		(1, '男性'),
	)

    gender = serializers.ChoiceField(label="性别", choices=gender_choice, default=1)
    phone_number = serializers.CharField(label="电话号码", max_length=20)
    occupation = serializers.CharField(label="职业", max_length=30)

    class Meta:
        model = UserInfo
        fields = "__all__"

class IllnessModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="疾病名称", max_length=30)

    class Meta:
        model = IllnessMode
        fields = "__all__"

class HealthRecordModelSerializer(serializers.ModelSerializer):
    user = UserInfoModelSerializer()
    height = serializers.IntegerField(label="身高")
    GI = serializers.FloatField(label="血糖指数")
    cholesterol = serializers.FloatField(label="胆固醇")
    UA = serializers.FloatField(label="尿酸指数")
    BP = serializers.FloatField(label="血压")

    illness = IllnessModelSerializer()

    class Meta:
        model = HealthRecord
        fields = "__all__"