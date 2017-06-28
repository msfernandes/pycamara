# -*- coding: utf-8 -*-
from dateutil import parser
from distutils.util import strtobool
from pycamara.exceptions import ClientError, ClientServerError
import pytz
import requests
import sys


if sys.version_info < (3, 0):  # pragma: no cover
    from urlparse import urljoin
else:  # pragma: no cover
    from urllib.parse import urljoin


class BaseClient(object):

    host = 'https://dadosabertos.camara.leg.br/api/v2/'

    def _get(self, path, **kwargs):
        return self._make_request('GET', path.strip('/'), kwargs)

    def _make_request(self, method, path, params):
        url = urljoin(self.host, path)
        headers = {'accept': 'application/json'}
        params['itens'] = 100
        response = requests.request(method, url, params=params,
                                    headers=headers)
        print(url)

        if not response.ok:
            error_json = response.json()
            msg = "[{0}]: {1} - {2}".format(error_json['status'],
                                            error_json['title'],
                                            error_json['detail'])
            raise ClientError(msg, response=response)

        response_json = response.json()
        next = None
        if 'links' in response_json and response_json['links']:
            for link in response_json['links']:
                if link['rel'] == 'next':
                    next = link['href'].replace(self.host, '')

        if next is not None:
            next_json = self._make_request(method, next, {})
            final_json = response_json['dados'] + next_json

        else:
            final_json = response_json['dados']
        return final_json

    def safe(self, element):
        if isinstance(element, list):
            safe_element = self._safe_list(element)
        elif isinstance(element, dict):
            safe_element = self._safe_dict(element)
        else:
            safe_element = self._safe_element(element)
        return safe_element

    def _safe_dict(self, dictionary):
        for key in dictionary.keys():
            dictionary[key] = self._safe_element(dictionary[key])

        return dictionary

    def _safe_element(self, element):
        if self._is_digit(element):
            safe_element = int(element)
        elif self._is_float(element):
            safe_element = float(element)
        elif self._is_bool(element):
            safe_element = bool(strtobool(element))
        elif isinstance(element, dict):
            safe_element = self._safe_dict(element)
        elif isinstance(element, list):
            safe_element = self._safe_list(element)
        else:
            safe_element = self._to_date_or_default(element)
        return safe_element

    def _safe_list(self, data_list):
        for index, element in enumerate(data_list):
            data_list[index] = self._safe_element(element)
        return data_list

    def _is_float(self, string):
        try:
            float(string)
            return True
        except (ValueError, TypeError):
            return False

    def _is_digit(self, string):
        try:
            int(string)
            return True
        except (ValueError, TypeError):
            return False

    def _is_bool(self, string):
        try:
            strtobool(string)
            return True
        except (ValueError, TypeError, AttributeError):
            return False

    def _to_date_or_default(self, string):
        final_value = None
        try:
            tz = pytz.timezone('America/Sao_Paulo')
            final_value = tz.localize(parser.parse(string))
        except (ValueError, TypeError):
            final_value = string.strip() if string else None
        return final_value
