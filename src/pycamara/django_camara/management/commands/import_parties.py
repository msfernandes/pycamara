from django.core.management.base import BaseCommand
from pycamara.django_camara.importers import parties


class Command(BaseCommand):

    def handle(self, *args, **options):
        parties.PartyImporter().save_data()
