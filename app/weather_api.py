from typing import List

import requests
from requests import HTTPError
from singleton import Singleton
from ipaddress import ip_address
from properties import TOKEN, LOCATION_BASE_URL, WEATHER_BASE_URL, FILTERED_FIELDS
from log import log

logger = log.setup_custom_logger('weather_api')


class IPWeatherFinder(metaclass=Singleton):

    @property
    def get_ipadress(self):
        return self._address

    def __init__(self, _address: str = None):
        self._address = _address
        self.session = requests.session()
        self.session.hooks = {'response': lambda r, *args, **kwargs: r.raise_for_status()}

    def _get_location_by_ipaddress(self) -> str:
        """

        :return: the city where the ipaddress is placed
        """
        response = self.session.get(f"{LOCATION_BASE_URL}{self._address}")
        location_info: dict = response.json()
        return location_info.get('city')

    @staticmethod
    def _filter_weather_info(fields: List[str], weather_info: dict) -> dict:
        """
        :param fields: gets rid of undesired parameters
        :param weather_info: the info obtained from the API
        :return: a dict with the filtered weather info
        """
        return {k: v for k, v in weather_info.items() if k not in fields}

    def get_weather(self) -> dict:
        """
        :return: a dict with the filtered weather info
        """
        try:
            location = self._get_location_by_ipaddress()
            response = self.session.get(f"{WEATHER_BASE_URL}{location}&appid={TOKEN}")
            weather_info = response.json()
            return self._filter_weather_info(FILTERED_FIELDS, weather_info)
        except HTTPError as err:
            logger.error(err)
            raise err
        except KeyError as kerr:
            logger.error(f"The response is not structured as expected")
            raise kerr

    def set_ipaddress(self, address: str) -> None:
        """

        :param address: checked to see if it is a valid IP value
        :return: None
        """
        ip_address(address)
        self._address = address
