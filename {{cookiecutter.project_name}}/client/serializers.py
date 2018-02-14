from rest_framework import serializers

from client.models import MyUser
from mylib.image import Base64ImageField


class MyUserSerializer(serializers.ModelSerializer):
    image=Base64ImageField(required=False,max_length=None,use_url=True)
    profile_image=serializers.SerializerMethodField()
    class Meta:
        model=MyUser
        fields=('id','first_name','last_name','google_profile_image','profile_image','username','image','password','dob','bio')
        extra_kwargs = {
            'password': {'write_only': True},
            # 'google_profile_image':{'write_only':True}
        }

    def get_profile_image(self,obj):
        defauly_image="http://pronksiapartments.ee/wp-content/uploads/2015/10/placeholder-face-big.png"
        if  obj.image:
            return obj.image
        if obj.google_profile_image:
            return obj.google_profile_image
        return defauly_image

    def create(self, validated_data):
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
