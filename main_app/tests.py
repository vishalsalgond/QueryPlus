from datetime import date
from django.contrib.auth.models import User
from .models import Question
from django.db.models import Max
from django.test import TestCase


class MainTestCase(TestCase):

    def setUp(self):

        # Create Users.
        u1 = User.objects.create(
            username="vishal2720",
            first_name="Vishal",
            last_name="Salgond",
            email="vns@google.com",
            password="vishal123"
        )

        # Create Questions.
        q1 = Question.objects.create(
            title="Sample question 1",
            question="This is question body",
            date_posted=date(2005, 7, 27),
            author=u1,
        )
        q1.upvotes.add(u1)

        q2 = Question.objects.create(
            title="Sample question 2",
            question="This is question body",
            date_posted=date(2005, 7, 25),
            author=u1
        )
        q2.downvotes.add(u1)

    def test_object_creation(self):
        """Test if objects are successfully created into the database."""
        self.assertEqual(Question.objects.count(), 2)

    def test_upvote_downvote(self):
        """One user cannot upvote and downvite the same question at the same time."""
        for q in Question.objects.all():
            for upvote in q.upvotes.all():
                for downvote in q.downvotes.all():
                    self.assertNotEqual(upvote, downvote)
