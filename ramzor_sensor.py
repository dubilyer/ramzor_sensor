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
    should_poll = True
    SCAN_INTERVAL = timedelta(seconds=5)
    native_value = None

    def __init__(self, city):
        self.city = city
        self.client = RamzorClient(city)
        logging.getLogger("ramz").warning(city)


    async def async_update(self):
        self.native_value = await self.hass.async_add_executor_job(self.client.get_latest_grade)
