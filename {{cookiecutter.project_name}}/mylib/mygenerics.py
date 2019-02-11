
from rest_framework.generics import GenericAPIView

from mylib.mymixins import MyCreateModelMixin, MyListModelMixin


from django.db import  models



class MyModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class MyListCreateAPIView(MyCreateModelMixin,MyListModelMixin,
                    GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



