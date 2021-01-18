from .entity import IntegrationBlueprintEntity
from homeassistant.core import CALLBACK_TYPE, HassJob, HomeAssistant, callback


class AddonSensor(IntegrationBlueprintEntity):
    """integration_blueprint Sensor class."""

    def __init__(self, coordinator, config_entry, slug):
        super().__init__(coordinator, config_entry)
        self.config_entry = config_entry
        self.slug = slug
        self._name = None

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}.{self.slug}"

    @property
    def name(self):
        """Return the name of the sensor."""
        for addon in self.coordinator.data.get("data").get("addons"):
            if addon["slug"] == self.slug:
                return addon["name"]

    @property
    def state(self):
        """Return the state of the sensor."""

        for addon in self.coordinator.data.get("data").get("addons"):
            if addon["slug"] == self.slug:
                if addon["update_available"] == True:
                    return "Update available"
                else:
                    return "Up to date"

        return (
            "Healthy"
            if self.coordinator.data is not None
            and self.coordinator.data.get("data").get("healthy") == True
            else "Not healthy"
        )

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:format-quote-close"
