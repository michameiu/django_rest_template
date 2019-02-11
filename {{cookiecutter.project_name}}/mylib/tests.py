from rest_framework.test import APITestCase, APIClient

from client.models import MyUser


class BaseAPITest(APITestCase):
    username = "michameiu@gmail.com"
    password = "micha"
    client_id = "iuyutyutuyctua"
    client_secret = "lahkckagkegigciegvjegvjhv"
    speaker = None

    def setUp(self):
        user = MyUser.objects.create(username=self.username)
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.user = user
        self.user.set_password(self.password)
        self.user.save()

