from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile
import pytesseract
from PIL import Image
from solver import solve as solver_solve
import logging


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
    prediction = ocr_prediction(img, one_line=True, compacted=True)
    if type(prediction) is str:
        return prediction
    return solve_inequation(prediction["text"])

@app.post("/solve", tags=["Solving"])
async def solve(inequation: str):
    return solve_inequation(inequation)

@app.post("/ocr", tags=["OCR"])
async def ocr(image: UploadFile, one_line: bool = True, compacted: bool = False):
    img = Image.open(image.file)
    return ocr_prediction(img, one_line=one_line, compacted=compacted)

def ocr_prediction(img: Image, one_line: bool = False, compacted: bool = False) -> Dict[str, str]:
    try:
        text = pytesseract.image_to_string(img)
        if one_line:
            text = one_line_process(text)
        if compacted:
            text = compacted_process(text)
        if len(text) > 0:
            logging.info("Readed:")
            logging.info(text)
            return {
                "text": text,
                # Info bug if dpi not perfect
                # "info": pytesseract.image_to_osd(img),
            }
        else:
            return "No text detected !"
    except:
        logging.error("Error trying to predict text !")
        return "Error trying to predict !"

def one_line_process(text: str) -> str:
    text = text.replace("\n", " ").replace("\f", "")
    while "  " in text:
        text = text.replace("  ", " ")
    return text

def compacted_process(text: str) -> str:
    return text.replace(" ", "")

def solve_inequation(inequation: str) -> Dict[str, str]:
    try:
        result: str = solver_solve(inequation)
        logging.info("Solved:")
        logging.info(inequation)
        logging.info(result)
        return {
            "base": inequation,
            "result": result.__str__(),
            "steps": None,
        }
    except:
        logging.error(f"Error trying to solve {inequation} !")
        return f"Error trying to solve {inequation} !"