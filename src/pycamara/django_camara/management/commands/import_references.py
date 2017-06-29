from django.core.management.base import BaseCommand
from pycamara.django_camara.importers import reference


class Command(BaseCommand):

    def handle(self, *args, **options):
        reference.CongressmanStatusImporter().save_data()
        reference.EventStatusImporter().save_data()
        reference.EventTypeImporter().save_data()
        reference.LegislativeBodyStatusImporter().save_data()
        reference.LegislativeBodyTypeImporter().save_data()
        reference.PropositionStatusImporter().save_data()
        reference.PropositionTypeImporter().save_data()
        reference.StatesImporter().save_data()
