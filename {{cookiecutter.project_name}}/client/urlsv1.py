from django.conf.urls import url

from client.views import RetrieveUpdateClient, CreateListUser

urlpatterns=[
    url(r'^$',CreateListUser.as_view(),name="create list clients"),
    url(r'^me/?$',RetrieveUpdateClient.as_view(),name="Retrieve_client"),
    url(r'^me/profile/?$',RetrieveUpdateClient.as_view(),name="Retrieve_client"),
]