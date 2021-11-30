from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity

from .ramzor_client import RamzorClient


class RamzorColor(SensorEntity):
    name = 'ramzor'
    unique_id = 'ramzor_12'
    entity_id = 'ramzor.color'
    device_info = 'israely ramzor'
    native_value = None

    def __init__(self, city):
        self.city = city
        self.client = RamzorClient(city)
        logging.getLogger("ramz").info(city)


    async def async_update(self):
        logging.getLogger("ramz").info("sending request info")
        self.native_value = await self.hass.async_add_executor_job(self.client.get_color)
