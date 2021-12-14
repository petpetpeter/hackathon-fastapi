import os
from typing import Optional

import requests
from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config


path = config('path')
# TODO: For local testing, comment out the above lines and uncomment the below line.
# path = 'test'

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/"+path)
def read_root():
    return {"Hello": "World"}


class Payload(BaseModel):
    url: str
    image_id: str


@app.post("/"+path+"/predict")
def predict(payload: Payload):
    # TODO: Deep learning & Machine learning code here. For example:
    # img_bytes = requests.get(payload.url).content
    # img = cv2.imdecode(np.asarray(bytearray(img_bytes), dtype=np.uint8), cv2.IMREAD_COLOR)

    # Example response must be like the below structure. If there is no bounding
    # boxes in the image, please return an empty list of "bbox_list".
    return {
        "image_id" : payload.image_id,
        "bbox_list": [
            {
                "category_id": 1,   # 1, 2, 3, or 4
                "bbox": {
                    "x": 0,         # top left (pixel)
                    "y": 220.666,   # top left (pixel)
                    "w": 1050.098,  # width (pixel)
                    "h": 525.333    # height (pixel)
                },
                "score": 0.635      # confidence score
            },
            {
                "category_id": 2,
                "bbox": {
                    "x": 123.456,
                    "y": 654.321,
                    "w": 112.112,
                    "h": 333.333
                },
                "score": 0.999
            }
        ]
    }
