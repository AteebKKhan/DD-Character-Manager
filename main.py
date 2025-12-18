import json

class Character:
    def __init__(self, name, level, vocation):
        self.name = name
        self.level = level
        self.vocation = vocation
        self.helmet = "None"
        self.body_armor = "None"
        self.gauntlets = "None"
        self.boots = "None"
        self.cape = "None"

    def set_equipment(self, helmet, body_armor, gauntlets, boots, cape):
        self.helmet = helmet
        self.body_armor = body_armor
        self.gauntlets = gauntlets
        self.boots = boots
        self.cape = cape

    def level_up(self):
        self.level += 1
        print(f"{self.name} has reached level {self.level}")

    def display_status(self):
        print(f"-- {self.name} --")
        print(f"-- Level: {self.level} --")
        print(f"-- Vocation: {self.vocation} --")
        print(f"-- Armor: {self.helmet}, {self.body_armor}, {self.gauntlets}, {self.boots}, {self.cape} --")

    def save_to_file(self):
        data = {
            "name": self.name,
            "level": self.level,
            "vocation": self.vocation,
            "equipment": {
                "helmet": self.helmet,
                "body_armor": self.body_armor,
                "gauntlets": self.gauntlets,
                "boots": self.boots,
                "cape": self.cape
            }
        }
        with open(f"{self.name}_save.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f" Progress saved for {self.name}!")

