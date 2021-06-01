from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from quizapp.views import login, pythonquiz, djangoquiz, register


# Create your tests here.
# -----------URL TESTING----------------#
class UrlTest(SimpleTestCase):
    def test_register_url_is_resolved(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_pythonquiz_url_is_resolved(self):
        url = reverse('pythonquiz')
        self.assertEquals(resolve(url).func, pythonquiz)

    def test_djangoquiz_url_is_resolved(self):
        url = reverse('djangoquiz')
        self.assertEquals(resolve(url).func, djangoquiz)


