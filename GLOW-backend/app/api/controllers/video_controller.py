from fastapi import APIRouter

router = APIRouter(prefix="/video", tags=["video"])

#for storing uploaded images in db and generating video
#use VideoDto for response and UploadedImagesDto for request body
@router.post("/generate-video")
def generate_video():
    return {"message": "Video generation endpoint"}


@router.get("/review-video")
def review_video():
    return {"message": "Video review endpoint"}


@router.post("/export-video")
def export_video():
    return {"message": "Video export endpoint"}


