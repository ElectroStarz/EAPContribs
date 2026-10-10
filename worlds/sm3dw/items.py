from __future__ import annotations
from enum import Enum

from typing import TYPE_CHECKING, NamedTuple

from Options import OptionError
from .options import *

from BaseClasses import Item, ItemClassification as IC


if TYPE_CHECKING:
    from . import SM3DWWorld

class SM3DWItem(Item):
    game = "Super Mario 3D World"

class ItemGroup(str, Enum):
    CHARACTERS = "Characters"
    WORLDS = "Worlds"
    UNLOCKS = "Unlocks"
    STARS = "Stars"
    FILLER = "Filler"
    TRAPS = "Traps"


class ItemData(NamedTuple):
    id: int
    classification: IC
    group: ItemGroup


characters = {
    "Mario": ItemData(1, IC.progression, ItemGroup.CHARACTERS),
    "Luigi": ItemData(2, IC.progression, ItemGroup.CHARACTERS),
    "Toad": ItemData(3, IC.progression, ItemGroup.CHARACTERS),
    "Peach": ItemData(4, IC.progression, ItemGroup.CHARACTERS),
    "Rosalina": ItemData(5, IC.progression, ItemGroup.CHARACTERS),
}

worlds = {
    "Progressive World": ItemData(52, IC.progression, ItemGroup.WORLDS),
    "World 1": ItemData(6, IC.progression, ItemGroup.WORLDS),
    "World 2": ItemData(7, IC.progression, ItemGroup.WORLDS),
    "World 3": ItemData(8, IC.progression, ItemGroup.WORLDS),
    "World 4": ItemData(9, IC.progression, ItemGroup.WORLDS),
    "World 5": ItemData(10, IC.progression, ItemGroup.WORLDS),
    "World 6": ItemData(11, IC.progression, ItemGroup.WORLDS),
    "World Castle": ItemData(12, IC.progression, ItemGroup.WORLDS),
    "World Bowser": ItemData(13, IC.progression, ItemGroup.WORLDS),
    "World Star": ItemData(14, IC.progression, ItemGroup.WORLDS),
    "World Flower": ItemData(15, IC.progression, ItemGroup.WORLDS),
    "World Mushroom": ItemData(16, IC.progression, ItemGroup.WORLDS),
    "World Crown": ItemData(17, IC.progression, ItemGroup.WORLDS),
}

unlocks = {
    "Plessy": ItemData(18, IC.progression, ItemGroup.UNLOCKS),
    "P-Switches": ItemData(19, IC.progression, ItemGroup.UNLOCKS),
    "?-! Switches": ItemData(20, IC.progression, ItemGroup.UNLOCKS),
    "Captain Toad": ItemData(21, IC.progression, ItemGroup.UNLOCKS),
    "Swapping Blocks": ItemData(22, IC.progression, ItemGroup.UNLOCKS),
    "Bomb Helmets": ItemData(23, IC.progression, ItemGroup.UNLOCKS),
    "Double Cherry": ItemData(24, IC.progression, ItemGroup.UNLOCKS),
    "Cat Suit": ItemData(25, IC.progression, ItemGroup.UNLOCKS),
    "Gold Cat Suit": ItemData(26, IC.progression, ItemGroup.UNLOCKS),
    "Fire Flower": ItemData(27, IC.progression, ItemGroup.UNLOCKS),
    "Boomerang Suit": ItemData(28, IC.progression, ItemGroup.UNLOCKS),
    "Helicopter Helmet": ItemData(29, IC.progression, ItemGroup.UNLOCKS),
    "Shoe Skis": ItemData(30, IC.useful, ItemGroup.UNLOCKS),
    "Goomba Helmet": ItemData(31, IC.useful, ItemGroup.UNLOCKS),
    "Green Star Coin Rings": ItemData(32, IC.progression, ItemGroup.UNLOCKS),
}

stars = {
    "World 1 Star": ItemData(33, IC.progression, ItemGroup.STARS),
    "World 2 Star": ItemData(34, IC.progression, ItemGroup.STARS),
    "World 3 Star": ItemData(35, IC.progression, ItemGroup.STARS),
    "World 4 Star": ItemData(36, IC.progression, ItemGroup.STARS),
    "World 5 Star": ItemData(37, IC.progression, ItemGroup.STARS),
    "World 6 Star": ItemData(38, IC.progression, ItemGroup.STARS),
    "World Castle Star": ItemData(39, IC.progression, ItemGroup.STARS),
    "World Bowser Star": ItemData(40, IC.progression, ItemGroup.STARS),
    "World Star Star": ItemData(41, IC.progression, ItemGroup.STARS),
    "World Flower Star": ItemData(42, IC.progression, ItemGroup.STARS),
    "World Mushroom Star": ItemData(43, IC.progression, ItemGroup.STARS),
    "World Crown Star": ItemData(44, IC.progression, ItemGroup.STARS),
    "Star": ItemData(45, IC.progression, ItemGroup.STARS),
}

filler = {
    "1-UP": ItemData(46, IC.filler, ItemGroup.FILLER),
    "15-UP": ItemData(47, IC.filler, ItemGroup.FILLER),
    "Random Powerup": ItemData(48, IC.filler, ItemGroup.FILLER),
    "Fill up Extra Power-Up Slot": ItemData(49, IC.filler, ItemGroup.FILLER),
}

traps = {
    "Smol Trap": ItemData(50, IC.trap, ItemGroup.TRAPS),
    "Bonk Trap": ItemData(51, IC.trap, ItemGroup.TRAPS),
}

item_table = {
    **characters,
    **worlds,
    **unlocks,
    **stars,
    **filler,
    **traps
}

ITEM_NAME_TO_ID: dict[str, int] = {item_name: data.id for item_name, data in item_table.items()}

def get_random_filler_item_name(world: SM3DWWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_percentage:
        return world.random.choice(list(traps))
    return world.random.choice(list(filler))

def create_item_with_correct_classification(world: SM3DWWorld, name: str) -> SM3DWItem:
    classification = item_table[name].classification

    return SM3DWItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

    #TODO if name == "World Crown" and world.options.

all_worlds_goals = [Goal.option_world_1, Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown]
post_world_1_goals = [Goal.option_world_4, Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown]
post_world_4_goals = [Goal.option_world_castle, Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown]
post_world_castle_goals = [Goal.option_world_bowser, Goal.option_world_flower, Goal.option_world_crown]
postgame_goals = [Goal.option_world_flower, Goal.option_world_crown]


def create_all_items(world: SM3DWWorld) -> None:

    itempool: list [Item] = [
        world.create_item("Plessy"),
        world.create_item("P-Switches"),
        world.create_item("?-! Switches"),
        world.create_item("Captain Toad"),
        world.create_item("Swapping Blocks"),
        world.create_item("Bomb Helmets"),
        world.create_item("Double Cherry"),
        world.create_item("Cat Suit"),
        world.create_item("Gold Cat Suit"),
        world.create_item("Fire Flower"),
        world.create_item("Boomerang Suit"),
        world.create_item("Helicopter Helmet"),
        world.create_item("Shoe Skis"),
        world.create_item("Goomba Helmet"),
        world.create_item("Green Star Coin Rings"),
    ]

    # Starting Character Option / Character Unlocks

    # Match & Case are just fancy if statements, match this variable to this number, if it matches, perform the indent
    match world.options.starting_character.value:
        case StartingCharacter.option_mario:
            starting = "Mario"
        case StartingCharacter.option_luigi:
            starting = "Luigi"
        case StartingCharacter.option_peach:
            starting = "Peach"
        case StartingCharacter.option_toad:
            starting = "Toad"
        case StartingCharacter.option_rosalina:
            starting = "Rosalina"
        case StartingCharacter.option_random_character:
            starting = world.random.choice(list(characters))
        case _:
            raise OptionError(f"Starting Character {world.options.starting_character.value} isn't valid!")

    world.push_precollected(world.create_item(starting))

    for character in characters:
        if character != starting:
            itempool.append(world.create_item(character))


    # goal = world.options.goal.value
    # split_stars = world.options.split_stars_by_world.value
    # world_rando = world.options.randomize_worlds.value
    #
    # #World Stars
    # if split_stars and goal in all_worlds_goals:
    #     #itempool.append(world.create_item("World 1 Star"))
    #     #loop that 24
    #     for i in range(24):
    #         itempool.append(world.create_item("World 1 Star"))
    #
    # elif split_stars and goal in post_world_1_goals:
    #
    #     for i in range(24):
    #         itempool.append(world.create_item("World 2 Star"))
    #     #loop 24
    #
    #     for i in range(31):
    #         itempool.append(world.create_item("World 3 Star"))
    #     #loop 31
    #
    #     for i in range(30):
    #         itempool.append(world.create_item("World 4 Star"))
    #     #loop 30
    #
    # elif split_stars and goal in post_world_4_goals:
    #     for i in range(31):
    #         itempool.append(world.create_item("World 5 Star"))
    #     #loop 31
    #
    #     for i in range(32):
    #         itempool.append(world.create_item("World 6 Star"))
    #     #loop 32
    #
    #     for i in range(32):
    #         itempool.append(world.create_item("World Castle Star"))
    #     #loop 32
    #
    # elif split_stars and goal in post_world_castle_goals:
    #     for i in range(39):
    #         itempool.append(world.create_item("World Bowser Star"))
    #     #loop 39
    #
    # elif split_stars and goal == postgame_goals:
    #     for i in range(32):
    #         itempool.append(world.create_item("World Star Star"))
    #     #loop 32
    #
    #     for i in range(31):
    #         itempool.append(world.create_item("World Flower Star"))
    #     #loop 31
    #
    #     for i in range(36):
    #         itempool.append(world.create_item("World Mushroom Star"))
    #     #loop 36
    #
    # elif split_stars and goal == Goal.option_world_crown:
    #     for i in range(38):
    #         itempool.append(world.create_item("World Crown Star"))
    #     #loop 38
    #
    # elif not split_stars and goal == Goal.option_world_1:
    #     for i in range(24):
    #         itempool.append(world.create_item("Star"))
    #     #loop 24
    #
    # elif not split_stars and goal == Goal.option_world_4:
    #     for i in range(109):
    #         itempool.append(world.create_item("Star"))
    #     #loop 109
    #
    # elif not split_stars and goal == Goal.option_world_castle:
    #     for i in range(204):
    #         itempool.append(world.create_item("Star"))
    #     #loop 204
    #
    # elif not split_stars and goal == Goal.option_world_bowser:
    #     for i in range(243):
    #         itempool.append(world.create_item("Star"))
    #     #loop 243
    #
    # elif not world.options.split_stars_by_world and goal == Goal.option_world_flower:
    #     for i in range(342):
    #         itempool.append(world.create_item("Star"))
    #     #loop 243 + Star (32) + Flower (31) + Mushroom (36)
    #
    # elif not split_stars and goal == Goal.option_world_crown:
    #     for i in range(380):
    #         itempool.append(world.create_item("Star"))
    #     #loop 243 + Star (32) + Flower (31) + Mushroom (36) + Crown (38)
    #
    # #Randomize Worlds
    # if world_rando and goal == Goal.option_world_1:
    #     itempool.append(world.create_item("World 1"))
    #
    # elif world_rando and goal == Goal.option_world_4:
    #     world_4_rand = world.random.randint(0, 2)
    #
    #     if world_4_rand == 0:
    #         starting_world_1 = world.create_item("World 1")
    #         world.push_precollected(starting_world_1)
    #
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #     elif world_4_rand == 1:
    #         starting_world_2 = world.create_item("World 2")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #     elif world_4_rand == 2:
    #         starting_world_3 = world.create_item("World 3")
    #         world.push_precollected(starting_world_3)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 4"))
    #
    # elif world_rando and goal == Goal.option_world_castle:
    #     world_castle_rand = world.randint(0, 5)
    #
    #     if world_castle_rand == 0:
    #         starting_world_1 = world.create_item("World 1")
    #         world.push_precollected(starting_world_1)
    #
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #
    #     elif world_castle_rand == 1:
    #         starting_world_2 = world.create_item("World 2")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #
    #     elif world_castle_rand == 2:
    #         starting_world_3 = world.create_item("World 3")
    #         world.push_precollected(starting_world_3)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #
    #     elif world_castle_rand == 3:
    #         starting_world_4 = world.create_item("World 4")
    #         world.push_precollected(starting_world_4)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #
    #     elif world_castle_rand == 4:
    #         starting_world_5 = world.create_item("World 5")
    #         world.push_precollected(starting_world_5)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #
    #     elif world_castle_rand == 5:
    #         starting_world_2 = world.create_item("World 6")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Castle"))
    #
    # elif world_rando and goal == Goal.option_world_bowser:
    #     world_bowser_rand = world.random.randint(0, 6)
    #
    #     if world_bowser_rand == 0:
    #         starting_world_1 = world.create_item("World 1")
    #         world.push_precollected(starting_world_1)
    #
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 1:
    #         starting_world_2 = world.create_item("World 2")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 2:
    #         starting_world_3 = world.create_item("World 3")
    #         world.push_precollected(starting_world_3)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 3:
    #         starting_world_4 = world.create_item("World 4")
    #         world.push_precollected(starting_world_4)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 4:
    #         starting_world_5 = world.create_item("World 5")
    #         world.push_precollected(starting_world_5)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 5:
    #         starting_world_6 = world.create_item("World 6")
    #         world.push_precollected(starting_world_6)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    #     elif world_bowser_rand == 6:
    #         starting_world_castle = world.create_item("World Castle")
    #         world.push_precollected(starting_world_castle)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Bowser"))
    #
    # elif world_rando and goal == Goal.option_world_flower:
    #     world_flower_rand = world.random.randint(0, 9)
    #
    #     if world_flower_rand == 0:
    #         starting_world_1 = world.create_item("World 1")
    #         world.push_precollected(starting_world_1)
    #
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 1:
    #         starting_world_2 = world.create_item("World 2")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 2:
    #         starting_world_3 = world.create_item("World 3")
    #         world.push_precollected(starting_world_3)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 3:
    #         starting_world_4 = world.create_item("World 4")
    #         world.push_precollected(starting_world_4)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 4:
    #         starting_world_5 = world.create_item("World 5")
    #         world.push_precollected(starting_world_5)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 5:
    #         starting_world_6 = world.create_item("World 6")
    #         world.push_precollected(starting_world_6)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 6:
    #         starting_world_castle = world.create_item("World Castle")
    #         world.push_precollected(starting_world_castle)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 7:
    #         starting_world_bowser = world.create_item("World Bowser")
    #         world.push_precollected(starting_world_bowser)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 8:
    #         starting_world_star = world.create_item("World Star")
    #         world.push_precollected(starting_world_star)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #
    #     elif world_flower_rand == 9:
    #         starting_world_flower = world.create_item("World Mushroom")
    #         world.push_precollected(starting_world_flower)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Flower"))
    #
    # elif world_rando and goal == Goal.option_world_crown:
    #     world_crown_rand = world.random.randint(0, 10)
    #
    #     if world_crown_rand == 0:
    #         starting_world_1 = world.create_item("World 1")
    #         world.push_precollected(starting_world_1)
    #
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 1:
    #         starting_world_2 = world.create_item("World 2")
    #         world.push_precollected(starting_world_2)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 2:
    #         starting_world_3 = world.create_item("World 3")
    #         world.push_precollected(starting_world_3)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 3:
    #         starting_world_4 = world.create_item("World 4")
    #         world.push_precollected(starting_world_4)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 4:
    #         starting_world_5 = world.create_item("World 5")
    #         world.push_precollected(starting_world_5)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 5:
    #         starting_world_6 = world.create_item("World 6")
    #         world.push_precollected(starting_world_6)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 6:
    #         starting_world_castle = world.create_item("World Castle")
    #         world.push_precollected(starting_world_castle)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 7:
    #         starting_world_bowser = world.create_item("World Bowser")
    #         world.push_precollected(starting_world_bowser)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 8:
    #         starting_world_star = world.create_item("World Star")
    #         world.push_precollected(starting_world_star)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 9:
    #         starting_world_flower = world.create_item("World Flower")
    #         world.push_precollected(starting_world_flower)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Mushroom"))
    #         itempool.append(world.create_item("World Crown"))
    #
    #     elif world_crown_rand == 10:
    #         starting_world_mush = world.create_item("World Mushroom")
    #         world.push_precollected(starting_world_mush)
    #
    #         itempool.append(world.create_item("World 1"))
    #         itempool.append(world.create_item("World 2"))
    #         itempool.append(world.create_item("World 3"))
    #         itempool.append(world.create_item("World 4"))
    #         itempool.append(world.create_item("World 6"))
    #         itempool.append(world.create_item("World Castle"))
    #         itempool.append(world.create_item("World Bowser"))
    #         itempool.append(world.create_item("World Star"))
    #         itempool.append(world.create_item("World 5"))
    #         itempool.append(world.create_item("World Flower"))
    #         itempool.append(world.create_item("World Crown"))
    #
    # elif not world.options.randomize_worlds and goal == Goal.option_world_1:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    # elif not world_rando and goal == Goal.option_world_4:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #
    # elif not world_rando and goal == Goal.option_world_castle:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #
    # elif not world_rando and goal == Goal.option_world_bowser:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #
    # elif not world_rando and goal == Goal.option_world_flower:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #
    # elif not world_rando and goal == Goal.option_world_crown:
    #     starting_progressive_world = world.create.item("Progressive World")
    #     world.push_precollected(starting_progressive_world)
    #
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))
    #     itempool.append(world.create_item("Progressive World"))

    goal = world.options.goal.value
    split_stars = world.options.split_stars_by_world.value
    world_rando = world.options.randomize_worlds.value

    # -------------------------
    # Star requirements
    # -------------------------

    def add_items(item_name, count):
        for _ in range(count):
            itempool.append(world.create_item(item_name))

    # Split Stars
    if split_stars:
        if goal in all_worlds_goals:
            star_counts = {"World 1 Star": 24}

        elif goal in post_world_1_goals:
            star_counts = {
                "World 2 Star": 24,
                "World 3 Star": 31,
                "World 4 Star": 30,
            }

        elif goal in post_world_4_goals:
            star_counts = {
                "World 5 Star": 31,
                "World 6 Star": 32,
                "World Castle Star": 32,
            }

        elif goal in post_world_castle_goals:
            star_counts = {"World Bowser Star": 39}

        elif goal == postgame_goals:
            star_counts = {
                "World Star Star": 32,
                "World Flower Star": 31,
                "World Mushroom Star": 36,
            }

        elif goal == Goal.option_world_crown:
            star_counts = {"World Crown Star": 38}

        else:
            star_counts = {}

    # Unsplit Stars
    else:
        star_totals = {
            Goal.option_world_1: 24,
            Goal.option_world_4: 109,
            Goal.option_world_castle: 204,
            Goal.option_world_bowser: 243,
            Goal.option_world_flower: 342,
            Goal.option_world_crown: 380,
        }

        star_counts = {"Star": star_totals[goal]} if goal in star_totals else {}

    for item_name, count in star_counts.items():
        add_items(item_name, count)

    # -------------------------
    # World randomization
    # -------------------------

    worlds_by_goal = {
        Goal.option_world_4: [
            "World 1", "World 2", "World 3", "World 4"
        ],
        Goal.option_world_castle: [
            "World 1", "World 2", "World 3", "World 4",
            "World 5", "World 6", "World Castle"
        ],
        Goal.option_world_bowser: [
            "World 1", "World 2", "World 3", "World 4",
            "World 5", "World 6", "World Castle", "World Bowser"
        ],
        Goal.option_world_flower: [
            "World 1", "World 2", "World 3", "World 4",
            "World 5", "World 6", "World Castle", "World Bowser",
            "World Star", "World Flower", "World Mushroom"
        ],
        Goal.option_world_crown: [
            "World 1", "World 2", "World 3", "World 4",
            "World 5", "World 6", "World Castle", "World Bowser",
            "World Star", "World Flower", "World Mushroom", "World Crown"
        ],
    }

    if world_rando:
        if goal == Goal.option_world_1:
            add_items("World 1", 1)

        elif goal in worlds_by_goal:
            all_worlds = worlds_by_goal[goal]

            # Preserve the original starting-world choices.
            starting_options = all_worlds[:-1]

            starting_world = starting_options[
                world.random.randint(0, len(starting_options) - 1)
            ]

            world.push_precollected(world.create_item(starting_world))

            # Add every other world
            for world_name in all_worlds:
                if world_name != starting_world:
                    itempool.append(world.create_item(world_name))


    # -------------------------
    # Progressive Worlds
    # -------------------------

    else:
        progressive_totals = {
            Goal.option_world_1: 1,
            Goal.option_world_4: 4,
            Goal.option_world_castle: 7,
            Goal.option_world_bowser: 8,
            Goal.option_world_flower: 11,
            Goal.option_world_crown: 12,
        }

        total = progressive_totals.get(goal, 0)

        if total:
            world.push_precollected(
                world.create_item("Progressive World")
            )

            add_items("Progressive World", total - 1)