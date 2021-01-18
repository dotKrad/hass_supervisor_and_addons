"""Binary sensor platform for integration_blueprint."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from .addonSensor import AddonSensor

from .const import (
    BINARY_SENSOR,
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_NAME,
    DOMAIN,
)
from .entity import IntegrationBlueprintEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    devices = []

    if coordinator.data != None:
        for addon in coordinator.data.get("data").get("addons"):
            print(addon["slug"])
            devices.append(AddonSensor(coordinator, entry, addon["slug"]))

    # async_add_devices([IntegrationBlueprintBinarySensor(coordinator, entry)])

    async_add_devices(devices)


class IntegrationBlueprintBinarySensor(IntegrationBlueprintEntity, BinarySensorEntity):
    """integration_blueprint binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
