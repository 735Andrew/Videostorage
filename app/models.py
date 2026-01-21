from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import INTERVAL

from app.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    video_path = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    duration = Column(INTERVAL, nullable=False)
    camera_number = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )