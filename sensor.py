from __future__ import annotations

import logging

import voluptuous as vol
from datetime import timedelta
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv

from .color_sensor import RamzorColor
from .ramzor_sensor import Ramzor

CITY = 'city'
CITIES = 'cities'

SCAN_INTERVAL = timedelta(hours=5)
should_poll = True

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CITY): cv.positive_int,
        vol.Optional(CITIES): cv.ensure_list(cv.positive_int)
    }
)


def setup_cities(config: ConfigType):
    try:
        cities = config[CITIES]
    except KeyError:
        cities = [setup_cities(config)]
    return cities


def setup_city(config: ConfigType):
    try:
        city = config[CITY]
    except KeyError:
        logging.getLogger("ramzor.logger").warning("City is not configured, running on Tel Aviv. Please read the "
                                                   "repository documentation here: "
                                                   "https://github.com/dubilyer/ramzor_sensor")
        city = 5000  # default city is Tel Aviv
    return city


def setup_platform(
        config: ConfigType,
        add_entities: AddEntitiesCallback):
    cities = setup_cities(config)
    for cty in cities:
        add_entities([
            Ramzor(cty),
            RamzorColor(cty)
        ], True)
