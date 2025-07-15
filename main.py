from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()

class InputData(BaseModel):
    encoded_string: str

@app.post("/decode")
async def decode_string(data: InputData):
    try:
        decoded_bytes = base64.b64decode(data.encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
        return {"decoded_data": decoded_string}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Decoding failed: {str(e)}")
