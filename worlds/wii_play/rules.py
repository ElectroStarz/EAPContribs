from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.rules import *
from .options import *
from .items import progressive_games

if TYPE_CHECKING:
    from . import WiiPlayWorld

def set_all_rules(world: "WiiPlayWorld") -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)

    set_goal_rules(world)
    set_completion_condition(world)

def set_completion_condition(world: "WiiPlayWorld") -> None:
    world.set_completion_rule(Has("Victory!"))

def set_all_entrance_rules(world: "WiiPlayWorld") -> None:

    games = ("Shooting Range", "Find Mii", "Table Tennis", "Pose Mii",
             "Laser Hockey", "Billiards", "Fishing", "Charge!", "Tanks!")

    for game in games:
        entrance = world.get_entrance(f"Main Menu -> {game}")
        world.set_rule(entrance, Has(game))

def set_all_location_rules(world: "WiiPlayWorld") -> None:
    # All of the Wii Play checks are in logic once you get into the region.
    # I plan to come back and add logic gates to Tanks! when missionsanity is enabled.
    pass

import math # Needed for the ceiling thingy in the medal hunt thingy

def set_goal_rules(world: "WiiPlayWorld") -> None:
    victory_location = world.get_location("Victory!")
    all_unlock_items = list(progressive_games.keys())
    goal = world.options.goal_type.value

    if goal in (GoalType.option_gold_medals, GoalType.option_platinum_medals):
        world.set_rule(victory_location, HasAll(*all_unlock_items))

    # elif goal == GoalType.option_platinum_medals:
    #     world.set_rule(victory_location, HasAll(*all_unlock_items))

    elif goal == GoalType.option_medal_hunt:
        medals_per_game = 4 if world.options.platinum_medals.value else 3
        games_needed = math.ceil(world.options.medal_hunt.value / medals_per_game)
        world.set_rule(victory_location, HasFromListUnique(*all_unlock_items, count=games_needed))

    elif goal == GoalType.option_tanks_100:
        world.set_rule(victory_location, Has("Tanks!"))