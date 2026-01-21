from datetime import datetime, timedelta
from typing import Literal

from pydantic import BaseModel, Field


class VideoAddSchema(BaseModel):
    video_path: str = Field(min_length=1)
    start_time: datetime
    duration: timedelta
    camera_number: int = Field(gt=0)
    location: str = Field(min_length=1)


class VideoSchema(VideoAddSchema):
    id: int
    status: Literal["new", "transcoded", "recognized"]

    class Config:
        from_attributes = True


class VideoUpdateSchema(BaseModel):
    status: Literal["new", "transcoded", "recognized"]
