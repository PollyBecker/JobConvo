from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class JobsUrlTests(TestCase):
    def test_home_job_url_is_correct(self):
        url=reverse('job:homepage')
        self.assertEqual(url, '/')

    def test_detalhe_job_url_is_correct(self):
        url= reverse('job:detalhe', args='1')
        self.assertEqual(url, "/jobs/1")


