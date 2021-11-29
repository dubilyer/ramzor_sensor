from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import PERCENTAGE

from .ramzor_client import RamzorClient


class Ramzor(SensorEntity):
    name = 'ramzor'
    unique_id = 'ramzor_123'
    entity_id = 'ramzor.super_senor'
    device_info = 'israely ramzor'
    unit_of_measurement = PERCENTAGE
    icon = None
    native_value = None

    def __init__(self, city):
        self.city = city
        self.client = RamzorClient(city)
        logging.getLogger("ramz").info(city)


    async def async_update(self):
        logging.getLogger("ramz").info("sending request info")
        self.native_value = await self.hass.async_add_executor_job(self.client.get_latest_grade)
