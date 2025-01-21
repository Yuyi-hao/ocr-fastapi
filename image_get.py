from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/get-image")
def get_image(request: Request):
    # return image
    image_path = "test_mg.png"
    return FileResponse(image_path, media_type="image/png")

if __name__=="__main__":
    uvicorn.run("image_get:app", port=8080, reload=True)