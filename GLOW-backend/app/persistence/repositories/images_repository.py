from sqlalchemy.orm import Session

class ImagesRepository:
    def __init__(self, db: Session):
        self.db = db

    async def save_image(self, image_id: int, image_data: bytes) -> dict:
        # Implement database logic to create an image record
        return {"message": f"Image {image_id} saved successfully"}


    async def get_images(self, collage_id: int) -> dict:
        # Implement database logic to retrieve images for a specific collage
        return {"collage_id": collage_id, "message": "Images retrieved successfully"}