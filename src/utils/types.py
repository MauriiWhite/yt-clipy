from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IeKey(str, Enum):
    YOUTUBE = "Youtube"


class TypeEnum(str, Enum):
    URL = "url"


class Thumbnail(BaseModel):
    url: str
    height: int
    width: int


class VideoSearchInfo(BaseModel):
    _type: TypeEnum
    ie_key: IeKey
    id: str
    url: str
    title: str
    description: Optional[str] = None
    duration: int
    channel_id: str
    channel: str
    channel_url: str
    uploader: str
    uploader_id: Optional[str] = None
    uploader_url: Optional[str] = None
    thumbnails: List[Thumbnail]
    timestamp: Optional[int] = None
    release_timestamp: Optional[int] = None
    availability: Optional[str] = None
    view_count: int
    live_status: Optional[str] = None
    channel_is_verified: Optional[bool] = None
    x_forwarded_for_ip: Optional[str] = None
