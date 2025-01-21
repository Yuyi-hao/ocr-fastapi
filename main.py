# url to text -> user url | text
# url to provide image -> url | image

from fastapi import FastAPI, Request, Body
import requests
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
OCR_API_KEY = os.getenv('OCR_API_KEY')

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "world"}

@app.post("/ocr-detection")
def get_ocr_detection(payload: dict = Body(...)):
    image_url = payload['url']
    
    # fetch image
    image_data = requests.get(image_url)
    if image_data.status_code == 200:
        image_data = image_data._content
    
    # send image to ocr analyzer
    analyzer_url = "https://api.ocr.space/parse/image"
    payload = {'isOverlayRequired': False,
               'apikey': OCR_API_KEY,
               'language': 'eng',
               }
    with open('test_mg.png', 'rb') as image_data:
        response = requests.post(analyzer_url, files={'image_data': image_data},data=payload)
    import json
    from pprint import pprint
    pprint(json.dumps(response._content.decode('utf-8').replace(r"\\", "")))

    return {
        "status": 200,
        "message": "OK",
        "content": {
            "image URL": image_url,
            # "image data": image_data,
            "data": "placeholder"
        }
    }



if __name__=="__main__":
    uvicorn.run("main:app", reload=True)