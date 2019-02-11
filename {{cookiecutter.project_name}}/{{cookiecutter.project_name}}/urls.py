"""template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


urlpatternsv1=[
    # url(r'^clients/',include('client.urlsV1')),
    # url(r'^games/',include('game.urlsV1')),
    url(r'^users/', include('client.urlsv1')),
]


#versions from the Apis(v1,v2)
apiversionsurlsparterns=[
    url(r'^v1/',include(urlpatternsv1))
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiversionsurlsparterns)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

]
