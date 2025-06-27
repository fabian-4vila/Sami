FROM python:3.12-alpine

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y portaudio19-dev && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
