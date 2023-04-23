class Appliance:
    def __init__(self, appliance):
        self.parent = appliance

    def data(self, data):
        if data["attributes"]["lastConnEvent"]["category"] == "DISCONNECTED":
            data["attributes"]["parameters"]["machMode"] = "0"
        data["active"] = bool(data.get("attributes", {}).get("activity"))
        return data

    def settings(self, settings):
        return settings
