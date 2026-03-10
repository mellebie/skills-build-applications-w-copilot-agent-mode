from django.core.management.base import BaseCommand
from octofit_tracker import models
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        models.User.objects.all().delete()
        models.Team.objects.all().delete()
        models.Activity.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Workout.objects.all().delete()

        # Create teams
        marvel = models.Team.objects.create(name='Team Marvel')
        dc = models.Team.objects.create(name='Team DC')

        # Create users
        ironman = models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = models.User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel)
        batman = models.User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = models.User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Create activities
        models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        models.Activity.objects.create(user=batman, type='cycle', duration=60, distance=20)

        # Create workouts
        models.Workout.objects.create(user=captain, description='Pushups', duration=15)
        models.Workout.objects.create(user=superman, description='Situps', duration=20)

        # Create leaderboard
        models.Leaderboard.objects.create(team=marvel, points=100)
        models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
