from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
import pytesseract
from PIL import Image


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/full", tags=["OCR", "Solving"])
async def full():
    return None

@app.post("/solve", tags=["Solving"])
async def solve(inequation: str):
    return None

@app.post("/ocr", tags=["OCR"])
async def ocr(image: UploadFile):
    img = Image.open(image.file)
    return {
            "text": pytesseract.image_to_string(img),
            "info": pytesseract.image_to_osd(img),
        }
