from django.core.management.base import BaseCommand
from django_pandas.io import read_frame
from base.models import ReactionTime

class Command(BaseCommand):
    help = 'Export reaction times to Excel'

    def handle(self, *args, **kwargs):
        # Load generators from Django model into DataFrame
        qs = ReactionTime.objects.all()
        df = read_frame(qs)

        # Save DataFrame to Excel file
        df.to_excel('base/files/reaction_times.xlsx', index=False)

        self.stdout.write('Reaction times generators has been exported to Excel.')
