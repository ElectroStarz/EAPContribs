from .dolphin_connection import *
from .mem_addresses import *
from enum import Enum

class ConnectionState(Enum):
    DISCONNECTED = 0
    CONNECTED = 1
    IN_MENU = 2

    # Games
    SHOOTING_RANGE = 3
    FIND_MII = 4
    TABLE_TENNIS = 5
    POSE_MII = 6
    LASER_HOCKEY = 7
    BILLIARDS = 8
    FISHING = 9
    CHARGE = 10
    TANKS = 11

class WiiPlayInterface:
    dolphin_client: DolphinClient
    connection_state: str
    logger: Logger

    def __init__(self, logger: Logger):
        self.logger = logger
        self.dolphin_client = DolphinClient(logger)


    def get_current_game(self) -> str | None:
        """Returns the string of the current game

        Returns None if no game active"""

        in_menu = bool(self.dolphin_client.read_word(GameState.menu_state))

        if not in_menu:
            current_game = self.dolphin_client.read_word(GameState.current_game)

            int_to_game = {
                0: "Shooting Range",
                1: "Find Mii",
                2: "Table Tennis",
                3: "Pose Mii",
                4: "Laser Hockey",
                5: "Billiards",
                6: "Fishing",
                7: "Charge!",
                8: "Tanks!"
            }

            return int_to_game[current_game]

        return None

    def in_menu(self) -> bool:
        """Returns True if the player is in the menu"""

        return bool(self.dolphin_client.read_word(GameState.menu_state))

    def is_paused(self) -> bool:
        """Returns True if the player is paused and NOT in the menu"""

        in_menu = bool(self.dolphin_client.read_word(GameState.menu_state))
        is_paused = bool(self.dolphin_client.read_word(GameState.pause_state))

        return is_paused and not in_menu

    def get_connection_state(self):
        try:
            if not self.dolphin_client.is_hooked():
                return ConnectionState.DISCONNECTED

            if self.in_menu():
                return ConnectionState.IN_MENU

            current_game = self.dolphin_client.read_word(GameState.current_game)

            int_to_state = {
                0: ConnectionState.SHOOTING_RANGE,
                1: ConnectionState.FIND_MII,
                2: ConnectionState.TABLE_TENNIS,
                3: ConnectionState.POSE_MII,
                4: ConnectionState.LASER_HOCKEY,
                5: ConnectionState.BILLIARDS,
                6: ConnectionState.FISHING,
                7: ConnectionState.CHARGE,
                8: ConnectionState.TANKS,
            }

            if current_game in int_to_state:
                return int_to_state[current_game]

            # Fallback, likely connected
            return ConnectionState.CONNECTED

        except (DolphinException, RuntimeError):
            return ConnectionState.DISCONNECTED