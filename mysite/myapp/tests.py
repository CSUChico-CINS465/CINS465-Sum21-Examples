from django.test import TestCase
from django.contrib.auth.models import User

from . import models

# Create your tests here.
class SuggestionTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        models.SuggestionModel.objects.create(suggestion="lion", author=user)
        models.SuggestionModel.objects.create(suggestion="cat", author=user)

    def test_suggestion_to_string(self):
        lion = models.SuggestionModel.objects.get(suggestion="lion")
        cat = models.SuggestionModel.objects.get(suggestion="cat")
        self.assertEqual(str(lion), "john lion")
        self.assertEqual(str(cat), "john cat")

class CommentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()
        sugg = models.SuggestionModel.objects.create(suggestion="lion", author=user)
        models.CommentModel.objects.create(comment="cat", author=user, suggestion=sugg)

    def test_suggestion_to_string(self):
        cat = models.CommentModel.objects.get(comment="cat")
        self.assertEqual(str(cat), "john cat")