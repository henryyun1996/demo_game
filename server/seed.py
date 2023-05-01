
# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Character, JobStats, Monster, MonsterStats, Inventory

# Constants
GENDERS = ("Male", "Female", "Non-binary")
SEXUAL_ORIENTATIONS = ("Straight", "Gay", "Lesbian", "Bisexual", "Asexual", "Pansexual")
JOBS = ("Knight", "Gunslinger", "Archer", "Thief", "Warrior", "Berserker", "Black Mage", "White Mage")
REGIONS = ("Nemar", "Cyneil", "Corize", "Naurra Isles", "Ausstero")
ITEM_NAME = "Potion"
ITEM_DESCRIPTION = "Restores 100 HP"
MAX_HP = 1000
MAX_LEVEL = 50
MAX_MG = 500
MAX_STATS = 100
MAX_QTY = 99

if __name__ == '__main__':
    fake = Faker()

    with app.app_context():
        print("Starting seed...")


        # Generate job stats for each job
        knight = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Knight",
            lvl=1,
            hp=620,
            mg=60,
            strg=50,
            defn=82,
            mind=75,
            intl=20,
            spd=25,
            evad=60,
        )
        gunslinger = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Gunslinger",
            lvl=1,
            hp=580,
            mg=90,
            strg=72,
            defn=68,
            mind=35,
            intl=35,
            spd=70,
            evad=70,
        )
        archer = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Archer",
            lvl=1,
            hp=540,
            mg=80,
            strg=70,
            defn=58,
            mind=45,
            intl=40,
            spd=90,
            evad=85,
        )
        thief = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Thief",
            lvl=1,
            hp=580,
            mg=60,
            strg=72,
            defn=55,
            mind=50,
            intl=48,
            spd=102,
            evad=100,
        )
        warrior = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Warrior",
            lvl=1,
            hp=670,
            mg=45,
            strg=80,
            defn=75,
            mind=30,
            intl=30,
            spd=60,
            evad=65,
        )
        berserker = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Berserker",
            lvl=1,
            hp=800,
            mg=20,
            strg=90,
            defn=50,
            mind=30,
            intl=30,
            spd=50,
            evad=55,
        )
        white_mage = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="White Mage",
            lvl=1,
            hp=520,
            mg=120,
            strg=30,
            defn=50,
            mind=80,
            intl=85,
            spd=45,
            evad=50,
        )
        black_mage = JobStats(
            job_image="https://drive.google.com/file/d/1-9E7n7FgvwLD1E2O3N0WM5bQfqeSk_Se/view?usp=sharing",
            job="Black Mage",
            lvl=1,
            hp=520,
            mg=120,
            strg=30,
            defn=50,
            mind=80,
            intl=85,
            spd=45,
            evad=50,
        )
        db.session.add_all([knight, gunslinger, archer, thief, warrior, berserker, white_mage, black_mage])

        # Generate bestiary
        for i in range(8):
            monster = Monster(
                monster_name=fake.first_name(),
            )
            db.session.add(monster)

        for monster in Monster.query.all():
            mon_stats = MonsterStats(
                hp=randint(100, MAX_HP),
                lvl=randint(1, MAX_LEVEL),
                mg=randint(50, MAX_MG),
                strg=randint(1, MAX_STATS),
                defn=randint(1, MAX_STATS),
                mind=randint(1, MAX_STATS),
                intl=randint(1, MAX_STATS),
                spd=randint(1, MAX_STATS),
                evad=randint(1, MAX_STATS),
                monster_id = monster.id,
            )
            db.session.add(mon_stats)

        db.session.commit()

        # # Weapons
        # iron_sword = Weapon("sword", 15, 0, "Iron Sword", "rom high-quality iron with a comfortable leather or cloth-wrapped hilt.")
        # iron_knife = Weapon("knife", 12, 0, "Iron Knife", "A small yet sharp weapon, commonly used for close combat and stealthy maneuvers")
        # iron_bow = Weapon("bow", 12, 0, "A sturdy bow crafted from high-quality iron with sturdy bowstrings to withstand heavy use.")
        # boltgun = Weapon("gun", 13, 0, "A reliable ranged weapon used for gunslingers.")
        # iron_ax = Weapon("ax", 18, 0, "A heavy weapon crafted from high-quality iron with a sturdy wooden or metal handle for better grip and control.")
        # iron_hammer = Weapon("hammer", 20, 0, "A reliable and sturdy weapon that can deliver powerful blows to enemies or shape metals and break through obstacles with ease.")
        # oak_wand = Weapon("wand", 3, 12, "A sturdy and reliable tool that is often associated with a strong mind.")
        # oak_staff = Weapon('staff', 2, 12, "A sturdy and reliable tool that is often associated with a strong mind.")

        # db.session.add()

        # # Armor
        # feather_cap = Armor("light", 8, 2, "Feather Cap", "A lightweight cap adorned with colorful feathers that enhances the wearer's agility and dexterity, making them more nimble in combat and easier to dodge incoming attacks.")
        # conical_hat = Armor("light", 4, 8, "Conical Hat", "A conical hat with a wide brim often worn by witches and other magic practitioners that enhances their magical abilities and protects them from the elements.")
        # leather_vest = Armor("light", 12, 2, "Leather Vest", "A durable vest made of thick leather that provides decent protection against physical attacks while allowing the wearer to remain agile and flexible in combat")
        # white_robe = Armor("light", 8, 12, "White Robe", "A flowing white robe often worn by holy men and women that enhances the wearer's magical abilities and provides some protection against dark magic")
        # black_robe = Armor("light", 8, 12, "Black Robe", "A dark robe that enhances the wearer's dark magic abilities")
        # leather_gloves = Armor("light", 6, 6, "Leather Gloves", "A pair of sturdy leather gloves that provide some protection to the wearer's hands.")
        # leather_boots = Armor("light", 8, 2, "Leather Boots" "A sturdy pair of leather boots that provide the wearer with both protection and agility.")
        # leather_sandels = Armor("light", 6, 6, "Leather Sandels", "A comfortable pair of leather sandals that allow the wearer's feet to breathe and move freely, providing greater mobility and comfort in warmer climates.")

        # db.session.add()

        # # Accessories
        # iron_bangle = Accessory(20, "Iron Bangle", "An iron bangel that adds +20 HP.")
        # circlet = Accessory(20, "Circlet", "An Circlet that adds +20 Intellect.")
        # power_bangle = Accessory(20, "Power Bangle" "An power bangel that adds +20 Strength.")
        # garnet = Accessory(20, "Garnet", "a powerful gemstone that grants +20 Mind")

        # db.session.add()

        # # Items
        # potion = Item(50, "Potion", "Restores 50 HP.")
        # mana = Item(50, "Mana", "Restores 50 MG.")

        # db.session.add()