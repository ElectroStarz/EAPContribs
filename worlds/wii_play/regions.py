from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import WiiPlayWorld

def create_and_connect_regions(world: "WiiPlayWorld") -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: "WiiPlayWorld") -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    billiards = Region("Billiards", world.player, world.multiworld)
    charge = Region("Charge!", world.player, world.multiworld)
    find_mii = Region("Find Mii", world.player, world.multiworld)
    fishing = Region("Fishing", world.player, world.multiworld)
    laser_hockey = Region("Laser Hockey", world.player, world.multiworld)
    pose_mii = Region("Pose Mii", world.player, world.multiworld)
    shooting_range = Region("Shooting Range", world.player, world.multiworld)
    table_tennis = Region("Table Tennis", world.player, world.multiworld)
    tanks = Region("Tanks!", world.player, world.multiworld)

    regions = [
        main_menu, billiards, charge, find_mii, fishing,
        laser_hockey, pose_mii, shooting_range, table_tennis, tanks,
    ]

    world.multiworld.regions += regions

def connect_regions(world: "WiiPlayWorld") -> None:
    main_menu = world.get_region("Main Menu")
    billiards = world.get_region("Billiards")
    charge = world.get_region("Charge!")
    find_mii = world.get_region("Find Mii")
    fishing = world.get_region("Fishing")
    laser_hockey = world.get_region("Laser Hockey")
    pose_mii = world.get_region("Pose Mii")
    shooting_range = world.get_region("Shooting Range")
    table_tennis = world.get_region("Table Tennis")
    tanks = world.get_region("Tanks!")

    main_menu.connect(billiards, "Main Menu -> Billiards")
    main_menu.connect(charge, "Main Menu -> Charge!")
    main_menu.connect(find_mii, "Main Menu -> Find Mii")
    main_menu.connect(fishing, "Main Menu -> Fishing")
    main_menu.connect(laser_hockey, "Main Menu -> Laser Hockey")
    main_menu.connect(pose_mii, "Main Menu -> Pose Mii")
    main_menu.connect(shooting_range, "Main Menu -> Shooting Range")
    main_menu.connect(table_tennis, "Main Menu -> Table Tennis")
    main_menu.connect(tanks, "Main Menu -> Tanks!")
