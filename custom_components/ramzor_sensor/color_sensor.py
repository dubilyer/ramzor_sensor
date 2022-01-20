from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity

from ramzor_client import RamzorClient


class RamzorColor(SensorEntity):
    name = 'ramzor_color'
    device_info = 'israely ramzor'
    unique_id = ''
    entity_id = ''
    native_value = None

    def __init__(self, city):
        self.city = city
        self.entity_id = 'ramzor.color_{}'.format(city)
        self.unique_id = 'ramzor.color_{}'.format(city)
        self.client = RamzorClient(city)
        logging.getLogger("ramzor.logger").info(city)

    async def async_update(self):
        logging.getLogger("ramzor.logger").info("sending request info")
        self.native_value = await self.hass.async_add_executor_job(self.client.get_color)
