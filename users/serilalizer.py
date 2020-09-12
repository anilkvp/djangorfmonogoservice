from rest_framework_mongoengine.serializers import DocumentSerializer
from users.models import User


class UserSerializer(DocumentSerializer):

    class Meta:
        model = User
        _fields = ('_id', 'username', 'password')

