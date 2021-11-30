from __future__ import annotations

import logging

import voluptuous as vol
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback, EntityPlatform
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

from .color_sensor import RamzorColor
from .ramzor_sensor import Ramzor

CITY= 'city'

SCAN_INTERVAL = timedelta(hours=5)
should_poll = True

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CITY): cv.positive_int,
    }
)

def setUpCity(config: ConfigType):
    try:
        city = config[CITY]
    except KeyError:
        logging.getLogger("ramzor.logger").warning("City is not configured, running on Tel Aviv. Please read the repostory documentation here: https://github.com/dubilyer/ramzor_sensor")
        city = 5000 # default city is Tel Aviv
    return city

def setup_platform(
        hass: HomeAssistant,
        config: ConfigType,
        add_entities: AddEntitiesCallback,
        discovery_info: DiscoveryInfoType):
    cty = setUpCity(config)
    add_entities([
        Ramzor(cty),
        RamzorColor(cty)
    ], True)

