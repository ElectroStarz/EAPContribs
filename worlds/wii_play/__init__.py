from collections.abc import Mapping
from typing import Any
from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from . import regions, rules, locations, items
from .options import *
from .items import ITEM_NAME_TO_ID
from .locations import LOCATION_NAME_TO_ID

class WiiPlayWebWorld(WebWorld):
    game = "Wii Play"
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Wii Play for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["synzic"],
    )

    tutorials = [setup_en]
    option_groups = wii_play_option_groups

class WiiPlayWorld(World):
    """
    """
    game = "Wii Play"
    web = WiiPlayWebWorld()

    options_dataclass = WiiPlayOptions
    options: WiiPlayOptions

    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    origin_region_name = "Main Menu"

    def generate_early(self) -> None:
        if self.options.goal_type.value == GoalType.option_platinum_medals and not self.options.platinum_medals.value:
            raise OptionError(
                f"{self.player_name}'s Goal Type is set to Platinum Medals, but Platinum Medals are not enabled!"
            )

        if (self.options.goal_type.value == GoalType.option_medal_hunt
                and not self.options.platinum_medals.value
                and self.options.medal_hunt.value > 27):
            raise OptionError(
                f"{self.player_name}'s Medal Hunt Amount is set above 27, but Platinum Medals is not enabled — "
                f"only 27 medals are possible without it!"
            )

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.WiiPlayItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal_type", "medal_hunt", "platinum_medals", "missionsanity",
            "tanks_missionsanity", "find_mii_challengesanity", "fishsanity",
            "foulsanity", "starting_games",
        )