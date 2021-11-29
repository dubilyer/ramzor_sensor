from __future__ import annotations
import voluptuous as vol
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback, EntityPlatform
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import homeassistant.helpers.config_validation as cv

from .ramzor_sensor import Ramzor
from homeassistant.components.sensor import PLATFORM_SCHEMA

CITY= 'city'

SCAN_INTERVAL = timedelta(seconds=5)
should_poll = True

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CITY): cv.positive_int,
    }
)

def setup_platform(
        hass: HomeAssistant,
        config: ConfigType,
        add_entities: AddEntitiesCallback,
        discovery_info: DiscoveryInfoType):
    add_entities([Ramzor(config[CITY])], True)

