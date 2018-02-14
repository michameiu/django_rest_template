from django.core.mail import send_mail
from django.db.models import Subquery, BooleanField
from django.db.models import Value
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.permissions import IsAuthenticated
from client.serializers import MyUserSerializer, GooglePlusSerializer
from models import MyUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,Group
from rest_framework import status
from permission import IsAuthenticatedOrPOSTOnly
from rest_framework import generics


#Email
def Email(client):
    print("sending email")
    rendered = render_to_string('email.html', {"user": client.name})
    ema = send_mail(
        subject='Welcome to Roometo',
        message="",
        html_message=rendered,
        from_email='Roometo Team <room@katanawebworld.com>',
        recipient_list=[client.username],
        fail_silently=False,
        # reply_to="room@katanawebworld.com"
    )
# Create your views here.


class CreateListUser(generics.CreateAPIView):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()



class RetrieveUpdateClient(generics.RetrieveUpdateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_object(self):
        return MyUser.objects.get(id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        sdata=self.get_update_data()
        instance = self.get_object()
        serializer = self.get_serializer(instance, data= sdata, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_update_data(self):
        ##Check if its from social login
        sdata=None
        type = self.request.query_params.get("type", None)
        if type == "google-plus":
            ser = GooglePlusSerializer(data=self.request.data)
            ser.is_valid(raise_exception=True)
            sdata = ser.data
        else:
            sdata=self.request.data
        return sdata


