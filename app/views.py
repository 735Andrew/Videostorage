from datetime import datetime
from typing import Literal, Annotated

from fastapi import APIRouter, Query, status, HTTPException

from app.schemas import VideoAddSchema, VideoSchema, VideoUpdateSchema
from app.service import VideoService

router = APIRouter(prefix="/videos")


@router.post("", response_model=VideoSchema, status_code=status.HTTP_201_CREATED)
async def add_video(video_data: VideoAddSchema):
    return await VideoService.add_video(video_data)


@router.get("", status_code=status.HTTP_200_OK)
async def find_videos(
    status: Literal["new", "transcoded", "recognized"] | None = None,
    camera_number: Annotated[str, Query(gt=0)] | None = None,
    location: Annotated[str, Query(min_length=1)] | None = None,
    video_path: Annotated[str, Query(min_length=1)] | None = None,
    start_time: datetime | None = None,
):
    q_parameters = {
        "status": status,
        "camera_number": camera_number,
        "location": location,
        "video_path": video_path,
        "start_time": start_time,
    }
    search_parameters = {key: value for key,value in q_parameters.items() if value is not None}

    return await VideoService.select_videos(search_parameters)


@router.get("/{video_id}", response_model=VideoSchema, status_code=status.HTTP_200_OK)
async def find_video(video_id: int):
    video = await VideoService.get_one(video_id)

    if video is None:
        raise HTTPException(
            detail=f"There is no video with id <{video_id}>",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return video


@router.patch(
    "/{video_id}/status",
    response_model=VideoSchema,
    status_code=status.HTTP_200_OK,
)
async def update_video(video_id: int, video_data: VideoUpdateSchema):
    video = await VideoService.get_one(video_id)

    if video is None:
        raise HTTPException(
            detail=f"There is no video with id <{video_id}>",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return await VideoService.update_video(video_id=video_id, status=video_data.status)
