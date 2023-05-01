from django.contrib.auth import get_user_model
#create serializers here
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"