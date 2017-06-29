from django.core.management.base import BaseCommand
from pycamara.django_camara.importers import legislative_bodies


class Command(BaseCommand):

    def handle(self, *args, **options):
        legislative_bodies.LegislativeBodyImporter().save_data()
