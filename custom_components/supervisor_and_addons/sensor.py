"""Sensor platform for integration_blueprint."""
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import IntegrationBlueprintEntity
from .supervisorSensor import SupervisorSensor
from .addonSensor import AddonSensor
from .totalUpdatesSensor import TotalUpdatesSensor

import pprint


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    devices = []
    # devices.append(IntegrationBlueprintSensor(coordinator, entry))
    devices.append(SupervisorSensor(coordinator, entry))

    devices.append(TotalUpdatesSensor(coordinator, entry))

    async_add_devices(devices)
    return


class IntegrationBlueprintSensor(IntegrationBlueprintEntity):
    """integration_blueprint Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return (
            "Healthy"
            if self.coordinator.data.get("data").get("healthy") == True
            else "Not healthy"
        )
        # return self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
