# -*- coding: utf-8 -*-
from django.db import transaction
import abc
import click


class BaseImporter(object):

    def __new__(cls):
        for field in cls.field_relation.keys():
            def _method(self, data):
                return data
            if not hasattr(cls, 'clean_' + field):
                setattr(cls, 'clean_' + field, _method)
        return super(BaseImporter, cls).__new__(cls)

    @abc.abstractmethod
    def get_data(self):
        return

    @abc.abstractmethod
    def get_model(self):
        return

    def get_progressbar_label(self):
        return 'Importing {0} data'.format(
            self.get_model()._meta.verbose_name_plural
        ).ljust(50)

    def after_save_object(self, obj):
        pass

    @transaction.atomic
    def save_data(self):
        data = self.get_data()
        if isinstance(data, dict):
            self._get_object(data)
        elif isinstance(data, list):
            with click.progressbar(data,
                                   label=self.get_progressbar_label()) as data:
                for data_row in data:
                    self._get_object(data_row)

    def _get_object(self, data):
        obj = self._fill_model(self.get_model(), data)
        self.after_save_object(obj)
        return obj

    def _fill_model(self, model_class, data):
        obj_dict = {}

        for field in self.field_relation.keys():
            try:
                clean_method = getattr(self, 'clean_' + field)
                key = self.field_relation[field]
                cleaned_field = clean_method(data.get(key, None))

                if cleaned_field == '':
                    cleaned_field = None

                obj_dict[field] = cleaned_field
            except KeyError:
                continue
        obj, created = model_class.objects.get_or_create(**obj_dict)
        return obj


class BaseDynamicDataImporter(BaseImporter):

    def __new__(cls, data):
        return super(BaseDynamicDataImporter, cls).__new__(cls)

    def __init__(self, data):
        self.data = data

    @transaction.atomic
    def save_data(self):
        data = self.data
        if isinstance(data, dict):
            self._get_object(data)
        elif isinstance(data, list):
            for data_row in data:
                self._get_object(data_row)
