from pyhon.appliances.base import ApplianceBase
from pyhon.parameter.fixed import HonParameterFixed


class Appliance(ApplianceBase):
    def attributes(self, data):
        data = super().attributes(data)
        if data["lastConnEvent"]["category"] == "DISCONNECTED":
            data["parameters"]["machMode"].value = "0"
        data["active"] = bool(data.get("activity"))
        data["pause"] = data["parameters"]["machMode"] == "3"
        return data

    def settings(self, settings):
        dry_level = settings.get("startProgram.dryLevel")
        if isinstance(dry_level, HonParameterFixed) and dry_level.value == "11":
            settings.pop("startProgram.dryLevel", None)
        return settings
