from rest_framework.viewsets import ModelViewSet
from .models import UserInfo, HealthRecord
from .serializers import UserInfoModelSerializer, HealthRecordModelSerializer
# Create your views here.
class UserInfoModelViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoModelSerializer

class HealthRecordModelViewSet(ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordModelSerializer