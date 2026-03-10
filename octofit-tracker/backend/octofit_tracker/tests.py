from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Workout.objects.create(user=batman, description='Situps', duration=20)
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Team.objects.count(), 2)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
