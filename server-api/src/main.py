from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile
import pytesseract
from PIL import Image
from solver import solve as solver_solve


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/full", tags=["OCR", "Solving"])
async def full(image: UploadFile):
    img = Image.open(image.file)
    return solve_inequation(ocr_prediction(img, one_line=True, compacted=True)["text"])

@app.post("/solve", tags=["Solving"])
async def solve(inequation: str):
    return solve_inequation(inequation)

@app.post("/ocr", tags=["OCR"])
async def ocr(image: UploadFile, one_line: bool = True, compacted: bool = False):
    img = Image.open(image.file)
    return ocr_prediction(img, one_line=one_line, compacted=compacted)

def ocr_prediction(img: Image, one_line: bool = False, compacted: bool = False) -> Dict[str, str]:
    text = pytesseract.image_to_string(img)
    if one_line:
        text = one_line_process(text)
    if compacted:
        text = compacted_process(text)
    return {
        "text": text,
        # Info bug if dpi not perfect
        # "info": pytesseract.image_to_osd(img),
    }

def one_line_process(text: str) -> str:
    text = text.replace("\n", " ").replace("\f", "")
    while "  " in text:
        text = text.replace("  ", " ")
    return text

def compacted_process(text: str) -> str:
    return text.replace(" ", "")

def solve_inequation(inequation: str) -> Dict[str, str]:
    print(solver_solve(inequation))
    return {
        "base": inequation,
        "result": solver_solve(inequation).__str__(),
        "steps": None,
    }