from django.core.management.base import BaseCommand
from pycamara.django_camara.importers import legislatures


class Command(BaseCommand):

    def handle(self, *args, **options):
        legislatures.LegislatureImporter().save_data()
