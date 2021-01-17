from .entity import IntegrationBlueprintEntity


class SupervisorSensor(IntegrationBlueprintEntity):
    """integration_blueprint Sensor class."""

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}.supervisor"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Supervisor"

    @property
    def state(self):
        """Return the state of the sensor."""
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