from sqlalchemy import select, insert, update

from app.database import async_session_maker
from app.models import Video
from app.schemas import VideoAddSchema, VideoSchema


class VideoService:

    @classmethod
    async def get_one(cls, video_id: int) -> VideoSchema:
        async with async_session_maker() as session:
            query = select(Video).filter_by(id=video_id)
            video = await session.execute(query)
            return video.scalar_one_or_none()

    @classmethod
    async def add_video(cls, video_data: VideoAddSchema) -> VideoSchema:
        async with async_session_maker() as session:
            data = video_data.model_dump()
            data["status"] = "new"

            query = insert(Video).values(**data).returning(Video)
            data = await session.execute(query)
            await session.commit()
            return data.scalar_one()

    @classmethod
    async def select_videos(cls, data:dict) -> VideoSchema:
        async with async_session_maker() as session:
            query = select(Video).filter_by(**data)
            data = await session.execute(query)
            return data.mappings().all()

    @classmethod
    async def update_video(cls, video_id: int, status: str) -> VideoSchema:
        async with async_session_maker() as session:
            query = (
                update(Video)
                .where(Video.id == video_id)
                .values(status=status)
                .returning(Video)
            )
            data = await session.execute(query)
            await session.commit()
            return data.scalar_one()
