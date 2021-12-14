from fastapi import FastAPI
from pydantic import BaseModel
from decouple import config

path = config('path')
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

  return {
    "image_id" : payload.image_id,
    "bbox_list": [{
        "category_id": 0,
        "bbox": {
          "x": 0,
          "y": 220.66666666666669, 
          "w": 1050.0986882341442,
          "h": 525.3333333333333
          },
        "score": 0.63508011493555
      }],
    }
