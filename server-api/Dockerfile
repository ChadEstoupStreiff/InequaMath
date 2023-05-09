FROM python:3.9.16-bullseye

# UPDATE
RUN pip install --upgrade pip
RUN apt-get update -y
RUN apt-get upgrade -y


# requirements
RUN apt install tesseract-ocr -y
RUN apt install libtesseract-dev -y
WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# APP
COPY src /app

# LAUNCH
WORKDIR /app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]