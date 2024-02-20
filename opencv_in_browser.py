import cv2
from fastapi import FastAPI, Response

app = FastAPI()

cap = cv2.VideoCapture(0)
def get_latest_image():
    frame_captured, frame = cap.read()
    if frame_captured:
        is_success, buffer = cv2.imencode(".jpg", frame)
        if is_success:
            return buffer.tobytes()

    return b'' 


@app.get("/")
async def root():
    image_bytes = get_latest_image()
    return Response(content=image_bytes, media_type="image/png")
