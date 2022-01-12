from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE

from .ramzor_client import RamzorClient


class Ramzor(SensorEntity):
    name = 'ramzor_grade'
    unique_id = ''
    entity_id = ''
    device_info = 'israeli ramzor'
    unit_of_measurement = PERCENTAGE
    native_value = None

    def __init__(self, city):
        self.city = city
        self.entity_id = 'ramzor.grade_{}'.format(city)
        self.unique_id = 'ramzor.grade_{}'.format(city)
        self.client = RamzorClient(city)
        logging.getLogger("ramzor.logger").info(city)

    async def async_update(self):
        logging.getLogger("ramzor.logger").info("sending request info")
        self.native_value = await self.hass.async_add_executor_job(self.client.get_latest_grade)
