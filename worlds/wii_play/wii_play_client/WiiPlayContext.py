import asyncio
import logging
import traceback
from collections import deque
from typing import Dict, Set, Optional, Any

from CommonClient import CommonContext, ClientCommandProcessor
from NetUtils import ClientStatus
from ..items import item_table
from ..locations import LOCATION_NAME_TO_ID

logger = logging.getLogger("Client")

ID_TO_NAME = {data.id: name for name, data in item_table.items()}
LOCATION_ID_TO_NAME = {loc_id: name for name, loc_id in LOCATION_NAME_TO_ID.items()}

CLIENT_VERSION = "0.0.1"