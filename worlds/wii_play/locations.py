from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple, Dict
from BaseClasses import Location, LocationProgressType as LPT
from . import items
from .options import *

if TYPE_CHECKING:
    from . import WiiPlayWorld

class WiiPlayLocation(Location):
    game = "Wii Play"

class LocData(NamedTuple):
    id: int
    location_type: LPT = LPT.DEFAULT

base_id = 0

shooting_range_locations = {
    "Shooting Range - Bronze Medal":        LocData(base_id + 1),
    "Shooting Range - Silver Medal":        LocData(base_id + 2),
    "Shooting Range - Gold Medal":          LocData(base_id + 3),
}

find_mii_locations = {
    "Find Mii - Bronze Medal":              LocData(base_id + 101),
    "Find Mii - Silver Medal":              LocData(base_id + 102),
    "Find Mii - Gold Medal":                LocData(base_id + 103),
}

find_mii_challengesanity_locations = {
    "Find Mii - Find 2 Look Alikes":        LocData(base_id + 151),
    "Find Mii - Find 3 Look Alikes":        LocData(base_id + 152),
    "Find Mii - Find 4 Look Alikes":        LocData(base_id + 153),
    "Find Mii - Find 5 Look Alikes":        LocData(base_id + 154),
    "Find Mii - Find the Odd Mii Out":      LocData(base_id + 155),
    "Find Mii - Find the Fastest Mii":      LocData(base_id + 156),
    "Find Mii - Find the Mii You're Using": LocData(base_id + 157),
    "Find Mii - Find This Mii":             LocData(base_id + 158),
    "Find Mii - Find the Sleepyhead":       LocData(base_id + 159),
    "Find Mii - Find Your Favorite":        LocData(base_id + 160),
}

pose_mii_locations = {
    "Pose Mii - Bronze Medal":              LocData(base_id + 201),
    "Pose Mii - Silver Medal":              LocData(base_id + 202),
    "Pose Mii - Gold Medal":                LocData(base_id + 203),
}

pose_mii_missionsanity_locations = {
    "Pose Mii - Stage 1 Complete":  LocData(base_id + 251),
    "Pose Mii - Stage 2 Complete":  LocData(base_id + 252),
    "Pose Mii - Stage 3 Complete":  LocData(base_id + 253),
    "Pose Mii - Stage 4 Complete":  LocData(base_id + 254),
    "Pose Mii - Stage 5 Complete":  LocData(base_id + 255),
    "Pose Mii - Stage 6 Complete":  LocData(base_id + 256),
    "Pose Mii - Stage 7 Complete":  LocData(base_id + 257),
    "Pose Mii - Stage 8 Complete":  LocData(base_id + 258),
    "Pose Mii - Stage 9 Complete":  LocData(base_id + 259),
    "Pose Mii - Stage 10 Complete": LocData(base_id + 260),
    "Pose Mii - Stage 11 Complete": LocData(base_id + 261),
    "Pose Mii - Stage 12 Complete": LocData(base_id + 262),
    "Pose Mii - Stage 13 Complete": LocData(base_id + 263),
    "Pose Mii - Stage 14 Complete": LocData(base_id + 264),
    "Pose Mii - Stage 15 Complete": LocData(base_id + 265),
}

laser_hockey_locations = {
    "Laser Hockey - Bronze Medal": LocData(base_id + 301),
    "Laser Hockey - Silver Medal": LocData(base_id + 302),
    "Laser Hockey - Gold Medal": LocData(base_id + 303),
}

table_tennis_locations = {
    "Table Tennis - Bronze Medal": LocData(base_id + 401),
    "Table Tennis - Silver Medal": LocData(base_id + 402),
    "Table Tennis - Gold Medal": LocData(base_id + 403),
}

fishing_locations = {
    "Fishing - Bronze Medal": LocData(base_id + 501),
    "Fishing - Silver Medal": LocData(base_id + 502),
    "Fishing - Gold Medal": LocData(base_id + 503),
}

fishing_fishsanity_locations = {
    "Fishing - Catch Plain Ol' Fish": LocData(base_id + 551),
    "Fishing - Catch Nibbler": LocData(base_id + 552),
    "Fishing - Catch Touchy Fish": LocData(base_id + 553),
    "Fishing - Catch King of the Pond": LocData(base_id + 554),
    "Fishing - Catch Mystery Fish": LocData(base_id + 555),
}

billiards_locations = {
    "Billiards - Bronze Medal": LocData(base_id + 601),
    "Billiards - Silver Medal": LocData(base_id + 602),
    "Billiards - Gold Medal": LocData(base_id + 603),
}

billiards_foulsanity_locations = {
    "Billiards - The cue ball fell into the pocket.": LocData(base_id + 651),
    "Billiards - The cue ball failed to hit the target ball first.": LocData(base_id + 652),
    "Billiards - The cue ball missed the target ball.": LocData(base_id + 653),
    "Billiards - You shot a ball off the table.": LocData(base_id + 654),
}

charge_locations = {
    "Charge! - Bronze Medal": LocData(base_id + 701),
    "Charge! - Silver Medal": LocData(base_id + 702),
    "Charge! - Gold Medal": LocData(base_id + 703),
}

tanks_locations = {
    "Tanks! - Bronze Medal": LocData(base_id + 1001),
    "Tanks! - Silver Medal": LocData(base_id + 1002),
    "Tanks! - Gold Medal": LocData(base_id + 1003),
}

tanks_missionsanity_locations = {
    "Tanks! - Mission 1 Complete": LocData(base_id + 1101),
    "Tanks! - Mission 2 Complete": LocData(base_id + 1102),
    "Tanks! - Mission 3 Complete": LocData(base_id + 1103),
    "Tanks! - Mission 4 Complete": LocData(base_id + 1104),
    "Tanks! - Mission 5 Complete": LocData(base_id + 1105),
    "Tanks! - Mission 6 Complete": LocData(base_id + 1106),
    "Tanks! - Mission 7 Complete": LocData(base_id + 1107),
    "Tanks! - Mission 8 Complete": LocData(base_id + 1108),
    "Tanks! - Mission 9 Complete": LocData(base_id + 1109),
    "Tanks! - Mission 10 Complete": LocData(base_id + 1110),
    "Tanks! - Mission 11 Complete": LocData(base_id + 1111),
    "Tanks! - Mission 12 Complete": LocData(base_id + 1112),
    "Tanks! - Mission 13 Complete": LocData(base_id + 1113),
    "Tanks! - Mission 14 Complete": LocData(base_id + 1114),
    "Tanks! - Mission 15 Complete": LocData(base_id + 1115),
    "Tanks! - Mission 16 Complete": LocData(base_id + 1116),
    "Tanks! - Mission 17 Complete": LocData(base_id + 1117),
    "Tanks! - Mission 18 Complete": LocData(base_id + 1118),
    "Tanks! - Mission 19 Complete": LocData(base_id + 1119),
    "Tanks! - Mission 20 Complete": LocData(base_id + 1120),
    "Tanks! - Mission 21 Complete": LocData(base_id + 1121),
    "Tanks! - Mission 22 Complete": LocData(base_id + 1122),
    "Tanks! - Mission 23 Complete": LocData(base_id + 1123),
    "Tanks! - Mission 24 Complete": LocData(base_id + 1124),
    "Tanks! - Mission 25 Complete": LocData(base_id + 1125),
    "Tanks! - Mission 26 Complete": LocData(base_id + 1126),
    "Tanks! - Mission 27 Complete": LocData(base_id + 1127),
    "Tanks! - Mission 28 Complete": LocData(base_id + 1128),
    "Tanks! - Mission 29 Complete": LocData(base_id + 1129),
    "Tanks! - Mission 30 Complete": LocData(base_id + 1130),
    "Tanks! - Mission 31 Complete": LocData(base_id + 1131),
    "Tanks! - Mission 32 Complete": LocData(base_id + 1132),
    "Tanks! - Mission 33 Complete": LocData(base_id + 1133),
    "Tanks! - Mission 34 Complete": LocData(base_id + 1134),
    "Tanks! - Mission 35 Complete": LocData(base_id + 1135),
    "Tanks! - Mission 36 Complete": LocData(base_id + 1136),
    "Tanks! - Mission 37 Complete": LocData(base_id + 1137),
    "Tanks! - Mission 38 Complete": LocData(base_id + 1138),
    "Tanks! - Mission 39 Complete": LocData(base_id + 1139),
    "Tanks! - Mission 40 Complete": LocData(base_id + 1140),
    "Tanks! - Mission 41 Complete": LocData(base_id + 1141),
    "Tanks! - Mission 42 Complete": LocData(base_id + 1142),
    "Tanks! - Mission 43 Complete": LocData(base_id + 1143),
    "Tanks! - Mission 44 Complete": LocData(base_id + 1144),
    "Tanks! - Mission 45 Complete": LocData(base_id + 1145),
    "Tanks! - Mission 46 Complete": LocData(base_id + 1146),
    "Tanks! - Mission 47 Complete": LocData(base_id + 1147),
    "Tanks! - Mission 48 Complete": LocData(base_id + 1148),
    "Tanks! - Mission 49 Complete": LocData(base_id + 1149),
    "Tanks! - Mission 50 Complete": LocData(base_id + 1150),
    "Tanks! - Mission 51 Complete": LocData(base_id + 1151),
    "Tanks! - Mission 52 Complete": LocData(base_id + 1152),
    "Tanks! - Mission 53 Complete": LocData(base_id + 1153),
    "Tanks! - Mission 54 Complete": LocData(base_id + 1154),
    "Tanks! - Mission 55 Complete": LocData(base_id + 1155),
    "Tanks! - Mission 56 Complete": LocData(base_id + 1156),
    "Tanks! - Mission 57 Complete": LocData(base_id + 1157),
    "Tanks! - Mission 58 Complete": LocData(base_id + 1158),
    "Tanks! - Mission 59 Complete": LocData(base_id + 1159),
    "Tanks! - Mission 60 Complete": LocData(base_id + 1160),
    "Tanks! - Mission 61 Complete": LocData(base_id + 1161),
    "Tanks! - Mission 62 Complete": LocData(base_id + 1162),
    "Tanks! - Mission 63 Complete": LocData(base_id + 1163),
    "Tanks! - Mission 64 Complete": LocData(base_id + 1164),
    "Tanks! - Mission 65 Complete": LocData(base_id + 1165),
    "Tanks! - Mission 66 Complete": LocData(base_id + 1166),
    "Tanks! - Mission 67 Complete": LocData(base_id + 1167),
    "Tanks! - Mission 68 Complete": LocData(base_id + 1168),
    "Tanks! - Mission 69 Complete": LocData(base_id + 1169),
    "Tanks! - Mission 70 Complete": LocData(base_id + 1170),
    "Tanks! - Mission 71 Complete": LocData(base_id + 1171),
    "Tanks! - Mission 72 Complete": LocData(base_id + 1172),
    "Tanks! - Mission 73 Complete": LocData(base_id + 1173),
    "Tanks! - Mission 74 Complete": LocData(base_id + 1174),
    "Tanks! - Mission 75 Complete": LocData(base_id + 1175),
    "Tanks! - Mission 76 Complete": LocData(base_id + 1176),
    "Tanks! - Mission 77 Complete": LocData(base_id + 1177),
    "Tanks! - Mission 78 Complete": LocData(base_id + 1178),
    "Tanks! - Mission 79 Complete": LocData(base_id + 1179),
    "Tanks! - Mission 80 Complete": LocData(base_id + 1180),
    "Tanks! - Mission 81 Complete": LocData(base_id + 1181),
    "Tanks! - Mission 82 Complete": LocData(base_id + 1182),
    "Tanks! - Mission 83 Complete": LocData(base_id + 1183),
    "Tanks! - Mission 84 Complete": LocData(base_id + 1184),
    "Tanks! - Mission 85 Complete": LocData(base_id + 1185),
    "Tanks! - Mission 86 Complete": LocData(base_id + 1186),
    "Tanks! - Mission 87 Complete": LocData(base_id + 1187),
    "Tanks! - Mission 88 Complete": LocData(base_id + 1188),
    "Tanks! - Mission 89 Complete": LocData(base_id + 1189),
    "Tanks! - Mission 90 Complete": LocData(base_id + 1190),
    "Tanks! - Mission 91 Complete": LocData(base_id + 1191),
    "Tanks! - Mission 92 Complete": LocData(base_id + 1192),
    "Tanks! - Mission 93 Complete": LocData(base_id + 1193),
    "Tanks! - Mission 94 Complete": LocData(base_id + 1194),
    "Tanks! - Mission 95 Complete": LocData(base_id + 1195),
    "Tanks! - Mission 96 Complete": LocData(base_id + 1196),
    "Tanks! - Mission 97 Complete": LocData(base_id + 1197),
    "Tanks! - Mission 98 Complete": LocData(base_id + 1198),
    "Tanks! - Mission 99 Complete": LocData(base_id + 1199),
    "Tanks! - Mission 100 Complete": LocData(base_id + 1200),
}

platinum_medal_locations = {
    "Shooting Range - Platinum Medal":  LocData(base_id + 4),
    "Find Mii - Platinum Medal":        LocData(base_id + 104),
    "Pose Mii - Platinum Medal":        LocData(base_id + 204),
    "Laser Hockey - Platinum Medal":    LocData(base_id + 304),
    "Table Tennis - Platinum Medal":    LocData(base_id + 404),
    "Fishing - Platinum Medal":         LocData(base_id + 504),
    "Billiards - Platinum Medal":       LocData(base_id + 604),
    "Charge! - Platinum Medal":         LocData(base_id + 704),
    "Tanks! - Platinum Medal":          LocData(base_id + 1004),
}

location_table = {
    **shooting_range_locations,
    **find_mii_locations,
    **find_mii_challengesanity_locations,
    **pose_mii_locations,
    **pose_mii_missionsanity_locations,
    **laser_hockey_locations,
    **table_tennis_locations,
    **fishing_locations,
    **fishing_fishsanity_locations,
    **billiards_locations,
    **billiards_foulsanity_locations,
    **charge_locations,
    **tanks_locations,
    **tanks_missionsanity_locations,
    **platinum_medal_locations,
}

LOCATION_NAME_TO_ID = {location_name: data.id for location_name, data in location_table.items()}

def create_all_locations(world: "WiiPlayWorld") -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: "WiiPlayWorld") -> None:
    shooting_range = world.get_region("Shooting Range")
    find_mii = world.get_region("Find Mii")
    pose_mii = world.get_region("Pose Mii")
    laser_hockey = world.get_region("Laser Hockey")
    table_tennis = world.get_region("Table Tennis")
    fishing = world.get_region("Fishing")
    billiards = world.get_region("Billiards")
    charge = world.get_region("Charge!")
    tanks = world.get_region("Tanks!")

    shooting_range.add_locations(
        get_location_names_with_ids(list(shooting_range_locations.keys())), WiiPlayLocation)
    find_mii.add_locations(
        get_location_names_with_ids(list(find_mii_locations.keys())), WiiPlayLocation)
    pose_mii.add_locations(
        get_location_names_with_ids(list(pose_mii_locations.keys())), WiiPlayLocation)
    laser_hockey.add_locations(
        get_location_names_with_ids(list(laser_hockey_locations.keys())), WiiPlayLocation)
    table_tennis.add_locations(
        get_location_names_with_ids(list(table_tennis_locations.keys())), WiiPlayLocation)
    fishing.add_locations(
        get_location_names_with_ids(list(fishing_locations.keys())), WiiPlayLocation)
    billiards.add_locations(
        get_location_names_with_ids(list(billiards_locations.keys())), WiiPlayLocation)
    charge.add_locations(
        get_location_names_with_ids(list(charge_locations.keys())), WiiPlayLocation)
    tanks.add_locations(
        get_location_names_with_ids(list(tanks_locations.keys())), WiiPlayLocation)

    # sanity options

    if world.options.find_mii_challengesanity:
        find_mii.add_locations(
            get_location_names_with_ids(list(find_mii_challengesanity_locations.keys())),
            WiiPlayLocation)

    if world.options.missionsanity in (Missionsanity.option_pose_mii, Missionsanity.option_both):
        pose_mii.add_locations(
            get_location_names_with_ids(list(pose_mii_missionsanity_locations.keys())),
            WiiPlayLocation)

    if world.options.fishsanity:
        fishing.add_locations(
            get_location_names_with_ids(list(fishing_fishsanity_locations.keys())),
            WiiPlayLocation)

    if world.options.foulsanity:
        billiards.add_locations(
            get_location_names_with_ids(list(billiards_foulsanity_locations.keys())),
            WiiPlayLocation)

    if world.options.missionsanity in (Missionsanity.option_tanks, Missionsanity.option_both):
        highest_mission = world.options.tanks_missionsanity.value
        gated_names = [
            f"Tanks! - Mission {mission} Complete"
            for mission in range(1, highest_mission + 1)
        ]
        tanks.add_locations(get_location_names_with_ids(gated_names), WiiPlayLocation)

    if world.options.platinum_medals:
        platinum_regions = {
            "Shooting Range - Platinum Medal": shooting_range,
            "Find Mii - Platinum Medal":       find_mii,
            "Pose Mii - Platinum Medal":       pose_mii,
            "Laser Hockey - Platinum Medal":   laser_hockey,
            "Table Tennis - Platinum Medal":   table_tennis,
            "Fishing - Platinum Medal":        fishing,
            "Billiards - Platinum Medal":      billiards,
            "Charge! - Platinum Medal":        charge,
            "Tanks! - Platinum Medal":         tanks,
        }
        for name, region in platinum_regions.items():
            region.add_locations(get_location_names_with_ids([name]), WiiPlayLocation)

def create_events(world: "WiiPlayWorld") -> None:
    main_menu = world.get_region("Main Menu")
    main_menu.add_event(
        "Victory!", "Victory!",
        location_type=WiiPlayLocation, item_type=items.WiiPlayItem,
    )

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int]:
    return {location_name: location_table[location_name].id for location_name in location_names}