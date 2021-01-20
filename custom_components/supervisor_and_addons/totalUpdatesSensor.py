from .entity import IntegrationBlueprintEntity


class TotalUpdatesSensor(IntegrationBlueprintEntity):
    """integration_blueprint Sensor class."""

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}.total_updates"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Total Updates"

    @property
    def state(self):
        """Return the state of the sensor."""

        total = 0
        if self.coordinator.data.get("data").get("update_available") == True:
            total = total + 1

        if self.coordinator.data is not None:
            for addon in self.coordinator.data.get("data").get("addons"):
                if addon["update_available"] == True:
                    total = total + 1

        return f"{total} pending update(s)"

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:format-quote-close"