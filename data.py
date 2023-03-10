#%%
all_units = [
    {
        "name": "Crystal Maiden",
        "races": ["Human"],
        "classes": ["Mage"],
        "cost": 1,
        "tier": 1,
    },
    {"name": "Axe", "races": ["Orc"], "classes": ["Warrior"], "cost": 1, "tier": 2},
    {
        "name": "Enchantress",
        "races": ["Beast"],
        "classes": ["Druid"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Hoodwink",
        "races": ["Beast"],
        "classes": ["Hunter"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Anti-mage",
        "races": ["Elf"],
        "classes": ["Demon Hunter"],
        "cost": 1,
        "tier": 1+1,
    },
    {"name": "Luna", "races": ["Elf"], "classes": ["Knight"], "cost": 1, "tier": 1},
    {"name": "Mirana", "races": ["Elf"], "classes": ["Hunter"], "cost": 1, "tier": 1},
    {
        "name": "Shadow Shaman",
        "races": ["Troll"],
        "classes": ["Shaman"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Witch Doctor",
        "races": ["Troll"],
        "classes": ["Warlock"],
        "cost": 1,
        "tier": 1,
    },
    {"name": "Dazzle", "races": ["Troll"], "classes": ["Priest"], "cost": 1, "tier": 1},
    {
        "name": "Vengeful Spirit",
        "races": ["Undead"],
        "classes": ["Demon Hunter"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Abaddon",
        "races": ["Undead"],
        "classes": ["Knight"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Winter Wyvern",
        "races": ["Undead", "Dragon"],
        "classes": ["Mage"],
        "cost": 1,
        "tier": 1+1,
    },
    {
        "name": "Clockwerk",
        "races": ["Goblin"],
        "classes": ["Mech"],
        "cost": 1,
        "tier": 1,
    },
    {"name": "Tinker", "races": ["Goblin"], "classes": ["Mech"], "cost": 1, "tier": 1},
    {
        "name": "Bounty Hunter",
        "races": ["Goblin"],
        "classes": ["Assassin"],
        "cost": 1,
        "tier": 1+1,
    },
    {
        "name": "Tiny",
        "races": ["Elemental"],
        "classes": ["Warrior"],
        "cost": 1,
        "tier": 1,
    },
    {"name": "Mars", "races": ["God"], "classes": ["Warrior"], "cost": 1, "tier": 1+1},
    {
        "name": "Spirit Breaker",
        "races": ["Tauren"],
        "classes": ["Assassin"],
        "cost": 1,
        "tier": 1,
    },
    {
        "name": "Beastmaster",
        "races": ["Orc"],
        "classes": ["Hunter"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Juggernaut",
        "races": ["Orc"],
        "classes": ["Warrior"],
        "cost": 2,
        "tier": 2+1,
    },
    {"name": "Ogre Magi", "races": ["Ogre"], "classes": ["Mage"], "cost": 2, "tier": 2},
    {
        "name": "Sniper",
        "races": ["Dwarf"],
        "classes": ["Hunter"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Puck",
        "races": ["Elf", "Dragon"],
        "classes": ["Mage"],
        "cost": 2,
        "tier": 2,
    },
    {"name": "Furion", "races": ["Elf"], "classes": ["Druid"], "cost": 2, "tier": 2},
    {
        "name": "Windranger",
        "races": ["Elf"],
        "classes": ["Hunter"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Batrider",
        "races": ["Troll"],
        "classes": ["Knight"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Timbersaw",
        "races": ["Goblin"],
        "classes": ["Mech"],
        "cost": 2,
        "tier": 2+1,
    },
    {
        "name": "Morphling",
        "races": ["Elemental"],
        "classes": ["Assassin"],
        "cost": 2,
        "tier": 2,
    },
    {"name": "Oracle", "races": ["God"], "classes": ["Priest"], "cost": 2, "tier": 2+1},
    {"name": "Slark", "races": ["Naga"], "classes": ["Assassin"], "cost": 2, "tier": 2},
    {
        "name": "Naga Siren",
        "races": ["Naga"],
        "classes": ["Wizard"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Chaos Knight",
        "races": ["Demon"],
        "classes": ["Knight"],
        "cost": 2,
        "tier": 2+1,
    },
    {"name": "Lion", "races": ["Demon"], "classes": ["Wizard"], "cost": 2, "tier": 2},
    {
        "name": "Centaur Warchief",
        "races": ["Centaur"],
        "classes": ["Warrior"],
        "cost": 2,
        "tier": 2+1,
    },
    {
        "name": "Brewmaster",
        "races": ["Pandaren"],
        "classes": ["Monk"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Faceless Void",
        "races": ["Faceless"],
        "classes": ["Assassin"],
        "cost": 2,
        "tier": 2,
    },
    {
        "name": "Legion Commander",
        "races": ["Human"],
        "classes": ["Knight"],
        "cost": 3,
        "tier": 3,
    },
    {"name": "Lina", "races": ["Human"], "classes": ["Mage"], "cost": 3, "tier": 3},
    {
        "name": "Treant Protector",
        "races": ["Elf"],
        "classes": ["Druid"],
        "cost": 3,
        "tier": 3,
    },
    {"name": "Marci", "races": ["Elf"], "classes": ["Monk"], "cost": 3, "tier": 3},
    {
        "name": "Phantom Assassin",
        "races": ["Elf"],
        "classes": ["Assassin"],
        "cost": 3,
        "tier": 3+1,
    },
    {
        "name": "Huskar",
        "races": ["Troll"],
        "classes": ["Warrior"],
        "cost": 3,
        "tier": 3+1,
    },
    {
        "name": "Pudge",
        "races": ["Undead"],
        "classes": ["Warrior"],
        "cost": 3,
        "tier": 3+1,
    },
    {
        "name": "Undying",
        "races": ["Undead"],
        "classes": ["Priest"],
        "cost": 3,
        "tier": 3,
    },
    {
        "name": "Razor",
        "races": ["Elemental"],
        "classes": ["Mage"],
        "cost": 3,
        "tier": 3,
    },
    {"name": "Rubick", "races": ["God"], "classes": ["Wizard"], "cost": 3, "tier": 3},
    {
        "name": "Slardar",
        "races": ["Naga"],
        "classes": ["Warrior"],
        "cost": 3,
        "tier": 3,
    },
    {
        "name": "Shadow Fiend",
        "races": ["Demon"],
        "classes": ["Warlock"],
        "cost": 3,
        "tier": 3+1,
    },
    {
        "name": "Terrorblade",
        "races": ["Demon"],
        "classes": ["Demon Hunter"],
        "cost": 3,
        "tier": 3+1,
    },
    {
        "name": "Sand King",
        "races": ["Aqir"],
        "classes": ["Assassin"],
        "cost": 3,
        "tier": 3,
    },
    {
        "name": "Venomancer",
        "races": ["Aqir", "Beast"],
        "classes": ["Warlock"],
        "cost": 3,
        "tier": 3,
    },
    {"name": "Meepo", "races": ["Kobold"], "classes": ["Mech"], "cost": 3, "tier": 3},
    {"name": "Riki", "races": ["Satyr"], "classes": ["Assassin"], "cost": 3, "tier": 3},
    {
        "name": "Keeper of the Light",
        "races": ["Human"],
        "classes": ["Mage"],
        "cost": 4,
        "tier": 4+1,
    },
    {
        "name": "Kunkka",
        "races": ["Human"],
        "classes": ["Warrior"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Dragon Knight",
        "races": ["Human", "Dragon"],
        "classes": ["Knight"],
        "cost": 4,
        "tier": 4+1,
    },
    {"name": "Chen", "races": ["Orc"], "classes": ["Priest"], "cost": 4, "tier": 4},
    {
        "name": "Lone Druid",
        "races": ["Beast"],
        "classes": ["Druid"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Monkey King",
        "races": ["Beast"],
        "classes": ["Monk"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Drow Ranger",
        "races": ["Undead"],
        "classes": ["Hunter"],
        "cost": 4,
        "tier": 4,
    },
    {"name": "Lich", "races": ["Undead"], "classes": ["Mage"], "cost": 4, "tier": 4},
    {
        "name": "Necrophos",
        "races": ["Undead"],
        "classes": ["Warlock"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Alchemist",
        "races": ["Goblin", "Ogre"],
        "classes": ["Warlock"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Snapfire",
        "races": ["Goblin"],
        "classes": ["Knight"],
        "cost": 4,
        "tier": 4,
    },
    {"name": "Medusa", "races": ["Naga"], "classes": ["Hunter"], "cost": 4, "tier": 4},
    {"name": "Doom", "races": ["Demon"], "classes": ["Warrior"], "cost": 4, "tier": 4},
    {
        "name": "Broodmother",
        "races": ["Aqir"],
        "classes": ["Hunter"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Earthshaker",
        "races": ["Tauren"],
        "classes": ["Shaman"],
        "cost": 4,
        "tier": 4,
    },
    {
        "name": "Magnus",
        "races": ["Centaur"],
        "classes": ["Assassin"],
        "cost": 4,
        "tier": 4,
    },
    {"name": "Warlock", "races": ["Orc"], "classes": ["Warlock"], "cost": 5, "tier": 5},
    {
        "name": "Disruptor",
        "races": ["Orc"],
        "classes": ["Shaman"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Primal Beast",
        "races": ["Beast"],
        "classes": ["Warrior"],
        "cost": 5,
        "tier": 5,
    },
    {"name": "Invoker", "races": ["Elf"], "classes": ["Mage"], "cost": 5, "tier": 5},
    {
        "name": "Templar Assassin",
        "races": ["Elf"],
        "classes": ["Assassin"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Spectre",
        "races": ["Undead"],
        "classes": ["Demon Hunter"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Troll Warlord",
        "races": ["Troll"],
        "classes": ["Warrior"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Gyrocopter",
        "races": ["Dwarf"],
        "classes": ["Mech"],
        "cost": 5,
        "tier": 5,
    },
    {"name": "Jakiro", "races": ["Dragon"], "classes": ["Mage"], "cost": 5, "tier": 5},
    {"name": "Techies", "races": ["Goblin"], "classes": ["Mech"], "cost": 5, "tier": 5},
    {
        "name": "Enigma",
        "races": ["Elemental"],
        "classes": ["Warlock"],
        "cost": 5,
        "tier": 5,
    },
    {"name": "Zeus", "races": ["God"], "classes": ["Mage"], "cost": 5, "tier": 5},
    {
        "name": "Elder Titan",
        "races": ["God", "Tauren"],
        "classes": ["Druid"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Tidehunter",
        "races": ["Naga"],
        "classes": ["Hunter"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Queen of Pain",
        "races": ["Demon"],
        "classes": ["Assassin"],
        "cost": 5,
        "tier": 5,
    },
    {
        "name": "Arc Warden",
        "races": ["Kobold"],
        "classes": ["Shaman"],
        "cost": 5,
        "tier": 5,
    },
]

all_combos = [
    {"requirement": (3, "Human"), "tier": 3},
    {"requirement": (6, "Human"), "tier": 3},
    {"requirement": (2, "Orc"), "tier": 2},
    {"requirement": (4, "Orc"), "tier": 2 + 1},
    {"requirement": (6, "Orc"), "tier": 2 + 1},
    {"requirement": (2, "Beast"), "tier": 2},
    {"requirement": (4, "Beast"), "tier": 2},
    {"requirement": (6, "Beast"), "tier": 2 + 2},
    {"requirement": (3, "Elf"), "tier": 3},
    {"requirement": (6, "Elf"), "tier": 3},
    {"requirement": (9, "Elf"), "tier": 3 + 2},
    {"requirement": (2, "Troll"), "tier": 2},
    {"requirement": (4, "Troll"), "tier": 2 + 1},
    {"requirement": (6, "Troll"), "tier": 2 + 2},
    {"requirement": (3, "Undead"), "tier": 3},
    {"requirement": (6, "Undead"), "tier": 3},
    {"requirement": (9, "Undead"), "tier": 3+1},
    {"requirement": (3, "Dragon"), "tier": 3},
    {"requirement": (5, "Dragon"), "tier": 2},
    {"requirement": (3, "Goblin"), "tier": 3},
    {"requirement": (6, "Goblin"), "tier": 3 + 2},
    {"requirement": (2, "Elemental"), "tier": 2},
    {"requirement": (4, "Elemental"), "tier": 2 + 1},
    {"requirement": (2, "God"), "tier": 2},
    {"requirement": (4, "God"), "tier": 2 + 1},
    {"requirement": (2, "Tauren"), "tier": 2},
    {"requirement": (4, "Tauren"), "tier": 2 + 1},
    {"requirement": (2, "Ogre"), "tier": 2},
    {"requirement": (2, "Dwarf"), "tier": 2},
    {"requirement": (2, "Naga"), "tier": 2},
    {"requirement": (4, "Naga"), "tier": 2 + 1},
    {"requirement": (6, "Naga"), "tier": 2 + 2},
    {
        "requirement": (1, "Demon"),
        "tier": 1,
        "synergies": [
            (
                2,
                "Demon Hunter",
                1,
            ),
        ],
        "note": "1demon=good, 2+demons require 2dh",
    },
    {"requirement": (2, "Centaur"), "tier": 2},
    {"requirement": (1, "Pandaren"), "tier": 1},
    {"requirement": (2, "Pandaren"), "tier": 1 + 2},
    {
        "requirement": (1, "Faceless"),
        "tier": 0,
        "note": "only active if no other synergies active",
    },
    {"requirement": (2, "Aqir"), "tier": 2},
    {"requirement": (4, "Aqir"), "tier": 2 + 2},
    {"requirement": (1, "Kobold"), "tier": 1},
    {"requirement": (2, "Kobold"), "tier": 1},
    {"requirement": (1, "Satyr"), "tier": 0},
    {"requirement": (3, "Mage"), "tier": 3},
    {"requirement": (6, "Mage"), "tier": 3 + 1},
    {"requirement": (9, "Mage"), "tier": 3 + 2},
    {"requirement": (3, "Warrior"), "tier": 3},
    {"requirement": (6, "Warrior"), "tier": 3 + 1},
    {"requirement": (9, "Warrior"), "tier": 3 + 2},
    {"requirement": (2, "Druid"), "tier": 2, "note": "well..."},
    {"requirement": (3, "Hunter"), "tier": 3},
    {"requirement": (6, "Hunter"), "tier": 3 + 1},
    {"requirement": (9, "Hunter"), "tier": 3 + 2},
    {"requirement": (2, "Demon Hunter"), "tier": 0},
    {"requirement": (4, "Demon Hunter"), "tier": 2 + 2},
    {"requirement": (2, "Knight"), "tier": 2},
    {"requirement": (4, "Knight"), "tier": 2 + 1},
    {"requirement": (6, "Knight"), "tier": 2 + 2},
    {"requirement": (3, "Mech"), "tier": 2},
    {"requirement": (6, "Mech"), "tier": 3 + 2},
    {"requirement": (3, "Assassin"), "tier": 3},
    {"requirement": (6, "Assassin"), "tier": 3 + 1},
    {"requirement": (9, "Assassin"), "tier": 3 + 1+1},
    {"requirement": (2, "Shaman"), "tier": 2},
    {"requirement": (4, "Shaman"), "tier": 2 + 1},
    {"requirement": (6, "Shaman"), "tier": 2 + 1+1},
    {"requirement": (2, "Priest"), "tier": 1-1, "note": "weird"},
    {"requirement": (4, "Priest"), "tier": 2-2, "note": "weird"},
    {"requirement": (2, "Warlock"), "tier": 1+1},
    {"requirement": (4, "Warlock"), "tier": 2 + 1},
    {"requirement": (6, "Warlock"), "tier": 2 + 1+1},
    {"requirement": (2, "Monk"), "tier": 2 + 1},
    {"requirement": (4, "Monk"), "tier": 2 + 1+1},
    {"requirement": (2, "Wizard"), "tier": 0+1+1},
    {"requirement": (4, "Wizard"), "tier": 1, "note": "weird"},
]
