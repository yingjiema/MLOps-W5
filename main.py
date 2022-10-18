from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/
app = FastAPI(title='Face FastAPI')

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    return {
        "face-bokeh": json.loads(requests.get("http://bokeh:8002/").text).get("message", ""),
        "face-emotion": json.loads(requests.get("http://emotion:8003/").text).get("message", ""),
    } 