from rest_framework import serializers


from client.models import MyUser
from mylib.image import Base64ImageField


class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField()
    new_password=serializers.CharField()

class AccountVerifySerializer(serializers.Serializer):
    token=serializers.CharField()
    confirm_code=serializers.IntegerField(allow_null=True)


class PasswordResetForEbnumeratorSerializer(serializers.Serializer):
    username=serializers.CharField()
    new_password=serializers.CharField()

class ForgotPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField()

    def validate_email(self,value):
        if MyUser.objects.filter(username=value).exists():
            return value
        raise serializers.ValidationError("user does not exist.")

class ResetPasswordserializer(serializers.Serializer):
    reset_code=serializers.IntegerField(required=True)
    new_password=serializers.CharField(required=True)

    def validate_reset_code(self,value):
        if not MyUser.objects.filter(reset_code=value).exists():
            raise serializers.ValidationError("Reset code Invalid or Expired")
        return value


class MyUserSerializer(serializers.ModelSerializer):
    # chart_settings=ChartSettingSerializer(many=True,read_only=True)
    image=Base64ImageField(required=False,max_length=None,use_url=True)
    profile_image=serializers.SerializerMethodField()
    gender_display=serializers.SerializerMethodField()
    class Meta:
        model=MyUser
        fields=("id","first_name","dummy","last_name","username",'dob','changed_password','role','image','email','phone','gender','password','profile_image','gender_display')
        extra_kwargs = {
            'password': {'write_only': True,"required":True},
            # 'google_profile_image':{'write_only':True}
        }

    def get_gender_display(self,obj):
        return obj.get_gender_display()

    def get_profile_image(self,obj):
        defauly_image="http://pronksiapartments.ee/wp-content/uploads/2015/10/placeholder-face-big.png"
        if  obj.image:
            return obj.image
        if obj.google_profile_image:
            return obj.google_profile_image
        return defauly_image

    def create(self, validated_data):
        # print(validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class GooglePlusSerializer(serializers.Serializer):
    familyName=serializers.CharField(max_length=45,required=False,allow_null=True)
    givenName=serializers.CharField(max_length=45,required=False,allow_null=True)
    imageUrl=serializers.URLField(max_length=200,required=False,allow_null=True)

    def to_representation(self, instance):

        return {"first_name":instance["givenName"],
                "last_name":instance["familyName"],

                "google_profile_image":instance["imageUrl"]
                }
