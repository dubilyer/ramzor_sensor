from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE

from .ramzor_client import RamzorClient


class Ramzor(SensorEntity):
    should_poll = True
    unit_of_measurement = PERCENTAGE
    SCAN_INTERVAL = timedelta(seconds=5)

    def __init__(self, city):
        self.city = city
        self._name = 'ramzor'
        self.entity_id = 'ramzor.grade'
        self.client = RamzorClient(city)
        logging.getLogger("ramz").info("ramzor is initialized with city ", city)


async def async_update(self):
    self.native_value = await self.hass.async_add_executor_job(self.client.get_latest_grade)
