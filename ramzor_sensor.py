from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE

from .ramzor_client import RamzorClient


class Ramzor(SensorEntity):
    name = 'ramzor_grade'
    unique_id = 'ramzor_11'
    device_info = 'israely ramzor'
    unit_of_measurement = PERCENTAGE
    native_value = None

    def __init__(self, city):
        self.city = city
        self.entity_id = 'ramzor.grade_{}'.format(city)
        self.client = RamzorClient(city)
        logging.getLogger("ramz").info(city)


    async def async_update(self):
        logging.getLogger("ramz").info("sending request info")
        self.native_value = await self.hass.async_add_executor_job(self.client.get_latest_grade)
