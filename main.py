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

    def save_to_file(self): #creates text file documenting new character data. plan to expand this further.
        newFile = "RPG_Data.txt"
        with open("RPG_Data.txt", "a") as f:
            f.write(f"Name of Character: {self.name} \n Vocation: {self.vocation} \n Level: {self.level}")
            f.write(f"Equipment: ")
            f.write(f"Helmet: {self.helmet} \n Body Armor: {self.body_armor} \n Gauntlets: {self.gauntlets} \n Boots: {self.boots} \n Cape: {self.cape}")


def main(arisenName, pawnName, pawnVocation, arisenVocation):
    arisen = Character(arisenName, 1, arisenVocation)
    mainPawn = Character(pawnName, 1, pawnVocation)

    print("--- RPG Character Manager ---")

    aoP = input("Manage the Arisen or your Pawn?")

    if aoP.lower() == "arisen":
        while True:
            print(f"\nCurrently Managing: {arisen.name}")
            print("1. Display status")
            print("2. Level up")
            print("3. Change Armor")
            print("4. Exit")

            choice = input("Select an option 1-4: ")

            if choice == "1":
                arisen.display_status()
            elif choice == "2":
                arisen.level_up()
            elif choice == "3":
                helmet = input("Enter helmet: ")
                body = input("Enter body armor: ")
                gauntlets = input("Enter gauntlets: ")
                boots = input("Enter boots: ") 
                cape = input("Enter cape: ")
                arisen.set_equipment(helmet, body, gauntlets, boots, cape)
                print("Equipment updated.")
            elif choice == "4":
                arisen.save_to_file()
                print("Safe travels!")  
                break 
            else:
                print("Invalid choice.")

    elif aoP.lower() == "pawn":
        while True:
            print(f"\nCurrently Managing: {mainPawn.name}")
            print("1. Display status")
            print("2. Level up")
            print("3. Change Armor")
            print("4. Exit")

            choice = input("Select an option 1-4: ")

            if choice == "1":
                mainPawn.display_status()
            elif choice == "2":
                mainPawn.level_up()
            elif choice == "3":
                helmet = input("Enter helmet: ")
                body = input("Enter body armor: ")
                gauntlets = input("Enter gauntlets: ")
                boots = input("Enter boots: ") 
                cape = input("Enter cape: ")
                mainPawn.set_equipment(helmet, body, gauntlets, boots, cape)
                print("Equipment updated.")
            elif choice == "4":
                arisen.save_to_file()   
                mainPawn.save_to_file()
                print("All party data saved. Safe travels!")  
                break
            else:
                print("Invalid choice.")

arisenName = input("Enter the name of your Arisen: ")
pawnName = input("Enter the name of your pawn: ")
print("--- The Vocations ---")
print("")
print(" Thief " \
" Sorcerer " \
" Warfarer " \
" Trickster " \
" Magick Archer " \
" Mage " \
" Warrior " \
" Mystic Spearhand " \
" Archer " \
" Fighter ")
arisenVocation = input("Enter your vocation: ")
pawnVocation = input("Enter your pawn's vocation: ")

print(main(arisenName, pawnName, pawnVocation, arisenVocation))
