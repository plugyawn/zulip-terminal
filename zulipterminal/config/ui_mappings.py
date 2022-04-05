from typing import Dict, Optional

from zulipterminal.api_types import EditPropagateMode
from zulipterminal.config.symbols import (
    STATUS_ACTIVE,
    STATUS_IDLE,
    STATUS_INACTIVE,
    STATUS_OFFLINE,
    BOT_MARKER
)


EDIT_MODE_CAPTIONS: Dict[EditPropagateMode, str] = {
    "change_one": "Change only this message topic",
    "change_later": "Also change later messages to this topic",
    "change_all": "Also change previous and following messages to this topic",
}


# Mapping that binds user activity status to corresponding markers.
STATE_ICON = {
    "active": STATUS_ACTIVE,
    "idle": STATUS_IDLE,
    "offline": STATUS_OFFLINE,
    "inactive": STATUS_INACTIVE,
    "bot": BOT_MARKER,
}


BOT_TYPE_BY_ID = {
    1: "Generic Bot",
    2: "Incoming Webhook Bot",
    3: "Outgoing Webhook Bot",
    4: "Embedded Bot",
}

BOT_ICON_BY_TYPE = {
    1: BOT_MARKER,
    2: BOT_MARKER,
    3: BOT_MARKER,
    4: BOT_MARKER,
}

ROLE_BY_ID: Dict[Optional[int], Dict[str, str]] = {
    100: {"bool": "is_owner", "name": "Owner"},
    200: {"bool": "is_admin", "name": "Administrator"},
    300: {"bool": "is_moderator", "name": "Moderator"},
    400: {"bool": "", "name": "Member"},
    600: {"bool": "is_guest", "name": "Guest"},
}

STREAM_POST_POLICY = {
    1: "Any user can post",
    2: "Only organization administrators can send to this stream",
    3: "Only organization administrators, moderators and full members can send to this stream",
    4: "Only organization administrators and moderators can send to this stream",
}
