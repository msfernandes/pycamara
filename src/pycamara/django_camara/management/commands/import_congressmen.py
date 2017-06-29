from django.core.management.base import BaseCommand
from pycamara.django_camara.importers import congressmen


class Command(BaseCommand):

    def handle(self, *args, **options):
        congressmen.CongressmanImporter().save_data()
