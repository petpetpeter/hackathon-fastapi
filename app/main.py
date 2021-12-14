from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config
import os


print(os.environ)
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
    # TODO: Deep learning & Machine leanring code here.

    # Example response must be like the below structure. If there is no bounding
    # boxes in the image, please return an empty list of "bbox_list".
    return {
        "image_id" : payload.image_id,
        "bbox_list": [
            {
                "category_id": 1,
                "bbox": {
                    "x": 0,
                    "y": 220.666,
                    "w": 1050.098,
                    "h": 525.333
                },
                "score": 0.635
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
