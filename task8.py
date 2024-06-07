class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return f"Name: {self.name},Age: {self.age},Gender: {self.gender},Super Power: {self.super_power},Weapon: {self.weapon}"

    def is_leader(self):
        return self.name in ["Captain America", "Iron Man"]


captain_america = Avenger("Captain America", 100, "Male", "Super strength", "Shield")
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 40, "Male", "Fighting skills", "Bow and Arrows")


print(captain_america.get_info())
print(f"Is {captain_america.name} a leader? {captain_america.is_leader()}")
