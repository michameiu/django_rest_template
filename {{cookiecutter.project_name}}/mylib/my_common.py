import boto3
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission

from {{cookiecutter.project_name}}.settings import DEFAULT_FROM_EMAIL

"""
from mylib.my_common import get_redirect_url

mylib.my_common.MyStandardPagination
get_redirect_url()
"""


class MyCustomException(APIException):
    status_code = 503
    detail = "Service temporarily unavailable, try again later."
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self, message, code=400):
        self.status_code = code
        self.default_detail = message
        self.detail = message


def get_digitalocean_spaces_download_url(filepath):
    # client = boto3.Session.client(boto3.Session(), 's3',
    #                               region_name=AWS_S3_REGION_NAME,
    #                               # endpoint_url=AWS_S3_ENDPOINT_URL,
    #                               aws_access_key_id=AWS_ACCESS_KEY_ID,
    #                               aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    #                               )
    # url = client.generate_presigned_url(ClientMethod='get_object',
    #                                     Params={'Bucket':AWS_STORAGE_BUCKET_NAME ,
    #                                             'Key': filepath},
    #                                     ExpiresIn=3000)
    return ""


class MyDjangoFilterBackend(DjangoFilterBackend):
    myfilter_class = None

    def get_filter_class(self, view, queryset=None):
        """
        Return the django-filters `FilterSet` used to filter the queryset.
        """
        if self.myfilter_class:
            return self.myfilter_class

        queryset = getattr(view, 'queryset', None)

        try:
            model = queryset.model
            filter_model = model
            # print("The filter class ...")
            filter_class = self.get_dynamic_filter_class(model)
            # print("The filter class ...")
            assert issubclass(queryset.model, filter_model), \
                'FilterSet model %s does not match queryset model %s' % \
                (filter_model, queryset.model)
            self.myfilter_class = filter_class
            return filter_class
        except Exception as e:
            raise MyCustomException("Dynamic Filter class error.")

    def get_dynamic_filter_class(self, model_class):

        class Meta:
            model = model_class
            exclude = ('file', 'image')  # [f.name for f in model_class.fields if  f.name in ["logo","image","file"]]
            fields = ("__all__")

        attrs = {"Meta": Meta,
                 }

        # myexcludes=["image","logo","file"]
        # myfields=[f.name for f in model_class.fields if  f.name in myexcludes]

        filter_class = type(model_class.__class__.__name__ + "FilterClass", (FilterSet,), attrs)
        # print(filter_class)
        return filter_class

"""
from mylib.my_common import MySendEmail as se

data={"verify_url":"Micha","name":"mwangi Micha","old_password":"hello"}
se("Test email","new_user.html",data,["michameiu@gmail.com"])

"""
def MySendEmail(subject, template, data, recipients, from_email=None):
    if from_email == None:from_email=DEFAULT_FROM_EMAIL
    rendered = render_to_string(template, data)
    ema = send_mail(
        subject=subject,
        message="",
        html_message=rendered,
        from_email=from_email,
        recipient_list=recipients,  # ['micha@sisitech.com'],
        fail_silently=False,
        # reply_to="room@katanawebworld.com"
    )


class MyStandardPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 1000
    page_size_query_param = 'page_size'


class MyIsAuthenticatedOrOptions(BasePermission):
    safe_methods = ["OPTIONS", ]

    def has_permission(self, request, view):
        if request.method in self.safe_methods:
            return True
        return request.user.is_authenticated()


def str2bool(value):
    trues = ["yes", "true", "1"]
    if value and value.lower() in trues:
        return True
    return False
