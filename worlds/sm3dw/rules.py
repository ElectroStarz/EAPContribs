from __future__ import annotations
from rule_builder.rules import *
from .options import *

if TYPE_CHECKING:
    from . import SM3DWWorld


def set_all_rules(world: SM3DWWorld):
    set_completion_condition(world)

def set_completion_condition(world: SM3DWWorld) -> None:
    world.set_completion_rule(Has("Victory!"))
    # Player is granted the "Victory!" item upon goaling